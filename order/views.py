# order/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from Menu.models import MenuItem
from .models import CartItem, Order , Cart , OrderItem
from django.views.generic import ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError


@method_decorator(login_required, name='dispatch')
class AddToCartView(View):
    template_name = 'menu/Menu_item_list.html'

    def post(self, request, item_id):
        item = get_object_or_404(MenuItem, id=item_id)
        quantity = int(request.POST.get('quantity', 1))

        # Retrieve or create the user's cart
        cart, created = Cart.objects.get_or_create(user=request.user)

        # Create a cart item and associate it with the cart
        cart_item, cart_item_created = CartItem.objects.get_or_create(
            cart=cart,
            item=item,
            user=request.user,
            defaults={'quantity': quantity}
        )

        # Optionally, update the quantity for the added item
        if not cart_item_created:
            cart_item.quantity += quantity
            cart_item.save()

        return redirect('Menu:menu_item_list')  # HTTP 204 No Content, assuming you're handling this via AJAX

@method_decorator(login_required, name='dispatch')
class ViewOrderView(View):
    template_name = 'order/view_order.html'

    def get(self, request, order_id):
        # Retrieve the order and associated order items
        order = get_object_or_404(Order, id=order_id, user=request.user)
        order_items = OrderItem.objects.filter(order=order)

        return render(request, self.template_name, {'order': order, 'order_items': order_items})

@method_decorator(login_required, name='dispatch')
class ViewCartView(View):
    template_name = 'order/view_cart.html'

    def get(self, request):
        # Retrieve the user's cart items
        cart_items = CartItem.objects.filter(user=request.user)
        
        # Check if the user has a cart, create one if not
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart.objects.create(user=request.user)

        # Calculate total price
        total_price = sum(cart_item.item.price * cart_item.quantity for cart_item in cart_items)
        payment_methods = Order.PAYMENT_METHOD_CHOICES

        return render(request, self.template_name, {'cart': cart, 'cart_items': cart_items, 'total_price': total_price , 'payment_methods': payment_methods})
    

    

@method_decorator(login_required, name='dispatch')
class PlaceOrderView(View):
    template_name = 'order/order_confirmation.html'

    def post(self, request):
        # Retrieve the user's cart items
        cart_items = CartItem.objects.filter(user=request.user)

        # Calculate total price
        total_price = sum(item.item.price * item.quantity for item in cart_items)

        # Extract form data
        dorm_number = request.POST.get('dorm_number')
        suggestion_box = request.POST.get('suggestion_box')
        payment_method = request.POST.get('payment_method')
        transaction_no = request.POST.get('transaction_no')

        try:
            # Create the order
            order = Order.objects.create(
                user=request.user,
                total_price=total_price,
                dorm_number=dorm_number,
                suggestion_box=suggestion_box,
                payment_method=payment_method,
                transaction_no=transaction_no
            )
        except IntegrityError as e :
            error_message = "Transaction number already exists!"
            cart_items = CartItem.objects.filter(user=request.user)
            cart = Cart.objects.get(user=request.user)
            total_price = sum(cart_item.item.price * cart_item.quantity for cart_item in cart_items)
            payment_methods = Order.PAYMENT_METHOD_CHOICES

            return render(request, 'order/view_cart.html' , {'cart': cart, 'cart_items': cart_items, 'total_price': total_price , 'payment_methods': payment_methods , 'error': error_message })
    

        # Associate the cart items with the order and calculate total price for each order item
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(
                order=order,
                item=cart_item.item,
                quantity=cart_item.quantity,
                total_price=cart_item.item.price * cart_item.quantity
            )

        # Clear the cart
        cart_items.delete()

        # Retrieve the order items for the current order
        order_items = OrderItem.objects.filter(order=order)

        return render(request, self.template_name, {'order': order, 'order_items': order_items})
@method_decorator(login_required, name='dispatch')
class DeleteItemView(View):
    def post(self, request, pk):
        cart_item = get_object_or_404(CartItem, pk=pk, user=request.user)
        cart_item.delete()
        return redirect('order:view_cart')
    
class OrderHistoryView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/order_history.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    

class AllOrderedItemsView(View):
    template_name = 'order/all_ordered_items.html'

    def get(self, request, *args, **kwargs):
        ordered_items = OrderItem.objects.filter(order__user=request.user)
        return render(request, self.template_name, {'ordered_items': ordered_items})



class OrderDetailsView(View):
    template_name = 'order/order_details.html'

    def get(self, request, order_id, *args, **kwargs):
        # Retrieve the order object
        order = get_object_or_404(Order, id=order_id)

        # Check if the user is the owner of the order or is an admin
        if request.user.is_superuser or request.user == order.user:
            order_items = OrderItem.objects.filter(order=order)
            return render(request, self.template_name, {'order': order, 'order_items': order_items})
        else:
            # User doesn't have permission to access this order
            raise PermissionDenied("You do not have permission to view this order.")
        

class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(check_payment=False)

class OrderChekeView(ListView):
    model = Order
    template_name = 'order/cheked_order.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(check_payment=True, order_delivered = False )
    

class MarkOrderDeliveredView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.order_delivered = True
        order.save()
        return redirect('order:order_cheke_list')
    
class MarkChekedView(View):
    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        order.check_payment = True
        order.save()
        return redirect('order:order_list')
    
class DeleteOrderView(LoginRequiredMixin, View):
    def post(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.delete()
        return redirect('order:order_list')