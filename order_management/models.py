from django.db import models
from user.models import User
from Menu.models import MenuItem

# order_management/models.py

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_management_orders')  # Add related_name
    # other fields

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='order_management_order_items')  # Add related_name
    # other fields
