#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework import routers


urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('', views.index, name='index'),
]