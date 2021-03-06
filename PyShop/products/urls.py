from django.urls import path
from . import views
# helps to map url to view function


urlpatterns = [
    path("", views.index),   # passing a reference , once the user call it , it will be activated
    path("new", views.new),
    path("cart/", views.cart, name='cart'),
    path("checkout/", views.checkout, ),
    path('<int:product_id>/', views.detail, name='detail'),

]