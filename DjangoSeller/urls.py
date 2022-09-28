"""DjangoSeller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('cart/', include('mycart.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', CreateView.as_view(
        template_name='registration/register.html',
        form_class=UserCreationForm,
        success_url='accounts/login'), name="register"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
