# menu/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models import Q  
from .models import MenuItem , Restaurant


def menu_item_list(request):
    # Assuming there's only one restaurant in the database
    restaurant = Restaurant.objects.first()
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    # Search functionality
    search_query = request.GET.get('search_query')
    if search_query:
        menu_items = menu_items.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    return render(request, 'Menu/menu_item_list.html', {'restaurant': restaurant, 'menu_items': menu_items})
