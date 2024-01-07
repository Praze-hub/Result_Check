from django.shortcuts import render
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly

class UserProfileListCreateView(generics.ListCreateAPIView):
    authentication_classes=[IsAuthorOrReadOnly]
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer

class UserProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[IsAuthorOrReadOnly]
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
