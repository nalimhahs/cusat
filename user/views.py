from django.shortcuts import render
from .models import CustomUser
from .forms import *
from order.models import Order

def user_dash_view(request):
    orders = Order.objects.filter(user_details__username=request.user.username)
    if(request.user.user_type == 'U'):
        return render(request, 'user/userhome.html', {'orders': orders})


