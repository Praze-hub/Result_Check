from django.shortcuts import render
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser




class UserProfileListCreateView(generics.ListCreateAPIView):

    permission_classes=(IsAuthorOrReadOnly,)
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

    

class UserProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    permission_classes=[IsAdminUser]
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
