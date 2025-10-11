from django.contrib import admin
from .models import Item, Order, Cart


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'state',)
    list_filter = ('state',)
    search_fields = ('user__email',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email',)
