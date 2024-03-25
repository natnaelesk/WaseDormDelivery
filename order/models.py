# order/models.py

from django.db import models
from user.models import User
from django.utils import timezone  # Import the timezone module
from Menu.models import MenuItem


class Order(models.Model):
    
    PAYMENT_METHOD_CHOICES = [
        ('CBE', 'CBE'),
    ]
      
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField(MenuItem, through='CartItem')
    order_delivered = models.BooleanField(default=False)
    dorm_number = models.PositiveIntegerField() 
    suggestion_box = models.TextField(blank=True)
    payment_method = models.CharField(max_length=50, choices=[('CBE', 'CBE')],blank=False)  # New field with choices
    transaction_no = models.TextField(unique=True , blank=False)
    check_payment = models.BooleanField(default=False)

    def __str__(self):
        return f"Order by {self.user.username} - {self.created_at}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class CartItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)  
    item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='CartItem')
    quantity = models.IntegerField(default=1)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    content = models.TextField()
    is_order_accepted = models.BooleanField(default=False)  # Flag to indicate if the message is related to order acceptance

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.recipient.username}"
    