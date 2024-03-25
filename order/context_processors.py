# order/context_processors.py

from .models import CartItem

def cart_length(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        cart_length = cart_items.count()  # Calculate the number of items in the cart
    else:
        cart_length = 0
    return {'cart_length': cart_length}
