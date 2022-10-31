from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import User
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import logout
from mycart.views import get_cart_size


def user_profile_page(request, user_id):
    template = "users/profile.html"
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, template, {'user': user, 'cart_size': get_cart_size(request)})


def user_registration_page(request):
    template = "users/register.html"
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('users:login')
        return HttpResponse(user_form.errors)
    else:
        user_form = UserRegistrationForm()
    return render(request, template, {'user_form': user_form})


def user_login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(email=data['email'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect("products:base")
            else:
                return HttpResponse('Invalid login')

    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


def user_logout_page(request):
    logout(request)
    return redirect('products:base')
