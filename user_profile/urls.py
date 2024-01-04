from django.urls import path
from .views import UserProfileListCreateView,UserProfileRetrieveUpdateDestroyView

urlpatterns=[
    path('userprofile/', UserProfileListCreateView.as_view(), name='userprofile-list-create'),
    path('userprofile/<int:pk>/', UserProfileRetrieveUpdateDestroyView.as_view(), name='userprofile-retrieve-update-delete'),
]