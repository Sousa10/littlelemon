#define URL route for index() view
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('menu/', views.MenuItemView.as_view(), name="get_menu"),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('', views.index, name='index'),
    path('api-token-auth/', obtain_auth_token)
]