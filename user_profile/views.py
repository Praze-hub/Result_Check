from django.shortcuts import render
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework import generics

class UserProfileListCreateView(generics.ListCreateAPIView):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

class UserProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
