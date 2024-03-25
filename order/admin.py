# order/admin.py

from django.contrib import admin
from .models import Order, CartItem
from .models import CartItem ,OrderItem



class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_price', 'created_at')
    inlines = [OrderItemInline]  # Include OrderItemInline
@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'item', 'quantity')
    list_filter = ('user', 'order', 'item')
    search_fields = ('user__username', 'item__name')  # Customize based on your model fields

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

admin.site.register(Order, OrderAdmin)