from django.contrib.auth import authenticate, login
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import User
from .forms import UserRegistrationForm, UserLoginForm, UserEditForm
from django.contrib.auth import logout
from django.views.generic.edit import UpdateView
from mycart.views import get_cart_size


def user_profile_page(request, user_id):
    template = "users/profile.html"
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    return render(request, template, {'user': user, 'cart_size': get_cart_size(request)})


def user_registration_page(request):
    if request.user.is_authenticated:
        return redirect("products:base")
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


class UserEditView(UpdateView):
    model = User
    template_name = "users/edit_profile.html"
    context_object_name = "user"
    fields = ['first_name', 'last_name']

    # form_class = UserEditForm

    def get_success_url(self):
        print("r2")
        return reverse('users:profile', kwargs={'user_id': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_edit_form'] = UserEditForm(instance=self.object)
        print(context)
        return context

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        form = UserEditForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('users:profile', user.pk)
        return HttpResponse(f"Form is not valid  {form.errors}")


def user_login_page(request):
    if request.user.is_authenticated:
        return redirect("products:base")
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(email=data['email'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect("products:base")
            form.add_error("email", "Your password or email doesn't match")
    else:
        form = UserLoginForm()
    print(form.errors)
    return render(request, 'users/login.html', {'form': form})


def user_logout_page(request):
    logout(request)
    return redirect('products:base')
