# menu/urls.py

from django.urls import path , include
from .views import menu_item_list

app_name = 'Menu'

urlpatterns = [
    path('', menu_item_list, name='menu_item_list'),
    path('order/', include(('order.urls', 'order'), namespace='order')),
    # Add more URLs for menu items, details, etc.
]
