


# order/urls.py
from django.urls import path
from .views import AddToCartView, DeleteOrderView ,MarkOrderDeliveredView , OrderChekeView , MarkChekedView , ViewCartView,OrderListView, PlaceOrderView  , DeleteItemView , ViewOrderView , OrderHistoryView , AllOrderedItemsView , OrderDetailsView

app_name = 'order'

urlpatterns = [  
    path('add_to_cart/<int:item_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('delete_item/<int:pk>/', DeleteItemView.as_view(), name='delete_item'),
    path('view_cart/', ViewCartView.as_view(), name='view_cart'),
    path('place_order/', PlaceOrderView.as_view(), name='place_order'),   
    path('view_order/<int:order_id>/', ViewOrderView.as_view(), name='view_order'),
    path('order_history/', OrderHistoryView.as_view(), name='order_history'), 
    path('order_list/', OrderListView.as_view(), name='order_list'),
    path('order_cheke_list/', OrderChekeView.as_view(), name='order_cheke_list'),
    path('order_details/<int:order_id>/', OrderDetailsView.as_view(), name='order_details'),
    path('mark_delivered/<int:pk>/', MarkOrderDeliveredView.as_view(), name='mark_delivered'),
    path('mark_cheked/<int:pk>/', MarkChekedView.as_view(), name='mark_cheked'),
     path('order/<int:pk>/delete/', DeleteOrderView.as_view(), name='delete_order'),
]
