from django.urls import path
from . import views
# helps to map url to view function


urlpatterns = [
    path("", views.index),   # passing a reference , once the user call it , it will be activated
    path("new", views.new),
    path('<int:product_id>/', views.detail, name='detail'),

]