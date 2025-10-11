from rest_framework import status, viewsets, pagination, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Item, Cart, Order
from .serializers import UserSerializer, ItemSerializer, CartSerializer, OrderSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class AuthorizationViewSet(viewsets.ViewSet):  # ViewSet pentru autentificare si inregistrare
    @action(methods=['POST'], detail=False)  # Endpoint POST pentru inregistrare
    def register(self, request):
        serializer = UserSerializer(data=request.data)  # Creeaza serializer cu datele primite
        if serializer.is_valid():  # Verifica daca datele sunt valide
            user = serializer.save()  # Salveaza utilizatorul nou
            refresh = RefreshToken.for_user(user)  # Genereaza token JWT pentru utilizator
            return Response({
                'refresh': str(refresh),  # Token refresh
                'access': str(refresh.access_token),  # Token access
                'email': user.email  # Emailul utilizatorului
            }, status=status.HTTP_201_CREATED)  # Raspuns cu status 201 (creat)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Raspuns cu erori si status 400

    @action(methods=['POST'], detail=False)  # Endpoint POST pentru login
    def login(self, request):
        email = request.data.get('email')  # Preia emailul din request
        password = request.data.get('password')  # Preia parola din request
        user = authenticate(request, username=email, password=password)  # Autentifica utilizatorul
        if user is not None:  # Daca autentificarea reuseste
            login(request, user)  # Logheaza utilizatorul
            refresh = RefreshToken.for_user(user)  # Genereaza token JWT
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'email': user.email
            }, status=status.HTTP_200_OK)  # Raspuns cu status 200 (ok)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  # Raspuns cu eroare 401

    @action(methods=['POST'], detail=False)  # Endpoint POST pentru logout
    def logout(self, request):
        logout(request)  # Delogheaza utilizatorul
        return Response(status=status.HTTP_200_OK)  # Raspuns cu status 200


class ItemViewSet(viewsets.ModelViewSet):  # ViewSet CRUD pentru produse
    queryset = Item.objects.all()  # Toate produsele din baza de date
    serializer_class = ItemSerializer  # Foloseste ItemSerializer pentru conversie
    pagination_class = pagination.LimitOffsetPagination  # Paginare pentru rezultate


class CartViewSet(viewsets.GenericViewSet):  # ViewSet pentru cosul de cumparaturi
    serializer_class = CartSerializer  # Foloseste CartSerializer
    authentication_classes = [JWTAuthentication]  # Doar utilizatori autentificati cu JWT
    permission_classes = [permissions.IsAuthenticated]  # Doar utilizatori logati

    @action(detail=False, methods=['post'])  # Endpoint POST pentru adaugare produs in cos
    def add_item(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)  # Ia sau creeaza cosul pentru user
        item_id = request.data.get('item_id')  # Preia id-ul produsului
        cart.items.add(item_id)  # Adauga produsul in cos
        serializer = self.get_serializer(cart)  # Serializare cos
        return Response(serializer.data)  # Raspuns cu cosul actualizat

    @action(detail=False, methods=['post'])  # Endpoint POST pentru eliminare produs din cos
    def remove_item(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)  # Ia sau creeaza cosul pentru user
        item_id = request.data.get('item_id')  # Preia id-ul produsului
        cart.items.remove(item_id)  # Elimina produsul din cos
        serializer = self.get_serializer(cart)  # Serializare cos
        return Response(serializer.data)  # Raspuns cu cosul actualizat

    @action(detail=False, methods=['get'])  # Endpoint GET pentru obtinere cos
    def get_cart(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)  # Ia sau creeaza cosul pentru user
        serializer = self.get_serializer(cart)  # Serializare cos
        return Response(serializer.data)  # Raspuns cu cosul


class OrderViewSet(viewsets.ModelViewSet):  # ViewSet CRUD pentru comenzi
    queryset = Order.objects.all()  # Toate comenzile din baza de date
    serializer_class = OrderSerializer  # Foloseste OrderSerializer
    authentication_classes = [JWTAuthentication]  # Doar utilizatori autentificati cu JWT
    permission_classes = [permissions.IsAuthenticated]  # Doar utilizatori logati

    @action(detail=False, methods=['post'])  # Endpoint POST pentru creare comanda noua
    def create_order(self, request):
        user = request.user  # Utilizatorul curent
        serializer = self.get_serializer(data=request.data)  # Serializare cu datele primite
        serializer.is_valid(raise_exception=True)  # Valideaza datele
        order = serializer.save(user=user)  # Creeaza comanda cu userul curent
        cart = Cart.objects.get(user=user)  # Ia cosul userului
        for item in cart.items.all():  # Pentru fiecare produs din cos
            order.items.add(item)  # Adauga produsul in comanda
        Cart.objects.filter(user=user).delete()  # Sterge cosul dupa plasarea comenzii
        serializer = self.get_serializer(order)  # Serializare comanda
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Raspuns cu comanda creata

    @action(detail=False, methods=['get'])  # Endpoint GET pentru comenzile userului
    def user_orders(self, request):
        user = request.user  # Utilizatorul curent
        orders = Order.objects.filter(user=user)  # Toate comenzile userului
        serializer = self.get_serializer(orders, many=True)  # Serializare lista comenzi
        return Response(serializer.data)  # Raspuns cu comenzile userului
