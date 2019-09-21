from django.shortcuts import render
from .models import CustomUser
from .forms import *
from order.models import Order

from order.forms import OrderForm

def user_dash_view(request):
    orders = Order.objects.filter(user_details=request.user).order_by('-date_of_order')
    if(request.user.user_type == 'U'):
        if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.user_details = request.user
                order.status = 'P'
                order.save()
                # return redirect()
        else:
            form = OrderForm()
        return render(request, 'user/userhome2.html', {'orders': orders, 'form': form})
