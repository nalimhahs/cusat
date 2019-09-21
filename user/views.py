from django.shortcuts import render
from .models import CustomUser
from .forms import *


def get_user_data(request):
    userdata = CustomUser.objects.filter(username=user.username)
    if(CustomUser.user_type == 'U'):
        return render(request, '', {'userdata': userdata})


def register_user_view(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = 'U'
            print(user.user_type)
            user.save()
            username = user.cleaned_data.get('email')
            raw_password = user.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
        else:
            form = UserRegistrationForm()
            print('here')

    return render(request, 'user/userreg.html', {'form': form})

