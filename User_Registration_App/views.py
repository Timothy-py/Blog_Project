from django.shortcuts import render, redirect
from User_Registration_App.forms import user_reg_form
from django.contrib import messages
from .forms import user_update_form, profile_update_form
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User

# Create your views here.

def user_registration(request):
    reg_form = user_reg_form()
    if request.method == 'POST':
        reg_form = user_reg_form(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            username = reg_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created succesfully {username}')
            return redirect('login')
    else:
        reg_form = user_reg_form()
    return render(request, 'User_Registration_App/registration_form.html', {'reg_form':reg_form})


@login_required
def user_profile(request):
    if request.method == 'POST':
        user_form = user_update_form(request.POST, instance=request.user)
        profile_form = profile_update_form(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            return redirect('')
    else:
        user_form = user_update_form(instance=request.user)
        profile_form = profile_update_form(instance=request.user.userprofile)
    return render(request, 'User_Registration_App/profile.html', {'form1':user_form, 'form2':profile_form})
