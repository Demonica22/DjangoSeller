from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('add/<data>',views.test_view, name="test")
]
