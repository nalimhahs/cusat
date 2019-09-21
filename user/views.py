from django.shortcuts import render
from .models import CustomUser
from .forms import *


def get_user_data(request):
    userdata = CustomUser.objects.filter(username=user.username)
    if(CustomUser.user_type == 'U'):
        return render(request, '', {'userdata': userdata})


def login_user_view(request):

    if request.method == 'POST':
        pass

    return render(request, 'user/userreg.html', {'form': form})

