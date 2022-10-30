from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('add_to_favourite/<int:user_id>/<int:product_id>', views.add_to_favourite, name="add_to_favourite"),
    path('favourite/<int:user_id>', views.favourite_products_page, name="favourite"),
]
