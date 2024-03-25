from django.shortcuts import render
from django.views import View
from order.models import Order , OrderItem
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404

class OrderListView(View):
    
    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'order_management/order_list.html', {'orders': orders})


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_management/order_detail.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = OrderItem.objects.filter(order=self.object)
        return context