from rest_framework.routers import DefaultRouter
from .views import AuthorizationViewSet, ItemViewSet, CartViewSet, OrderViewSet

app_name = "online_store"

router = DefaultRouter()
router.register(r'authorization', AuthorizationViewSet, basename='authorization')
router.register(r'items', ItemViewSet, basename='items')
router.register(r'cart', CartViewSet, basename='cart')
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    
]

urlpatterns += router.urls