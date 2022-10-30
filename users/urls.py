from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('<int:user_id>', views.user_profile_page, name='profile'),
    path('registration', views.user_registration_page, name="registration"),
    path('login', views.user_login_page, name='login'),
    path('logout', views.user_logout_page, name='logout'),
]
