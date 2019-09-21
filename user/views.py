from django.shortcuts import render
from .models import CustomUser

def get_user_data(request):
    userdata=CustomUser.objects.filter(username=user.username)
    if(CustomUser.user_type=='U'):
        return render(request,'',{'userdata':userdata})
