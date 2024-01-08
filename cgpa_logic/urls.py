from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CGPACalculator



# router = DefaultRouter()
# router.register(r'courses', CourseViewSet)



urlpatterns = [
    path('', CGPACalculator.as_view(), name='calculate_cgpa'),
]
