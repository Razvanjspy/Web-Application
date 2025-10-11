from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from online_store.models import Item, Cart, Order

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', "first_name", "last_name"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        return user


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items']


class OrderSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'items', 'first_name', 'last_name', 'city', 'country', 'address_details', 'date']

    def validate(self, attrs):
        if not attrs.get('first_name'):
            raise ValidationError({'first_name': 'First name is required.'})

        if not attrs.get('last_name'):
            raise ValidationError({'last_name': 'Last name is required.'})

        if not attrs.get('city'):
            raise ValidationError({'city': 'City is required.'})

        if not attrs.get('country'):
            raise ValidationError({'country': 'Country is required.'})

        if not attrs.get('address_details'):
            raise ValidationError({'address_details': 'Address details are required.'})

        return attrs

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        return order
