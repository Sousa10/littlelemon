from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MenuItemView(generics.ListCreateAPIView, generics.UpdateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.CreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer