from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import  Course
from .serializers import CourseSerializer
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.functional import SimpleLazyObject



class CGPACalculator(APIView):
    def post(self, request, format=None):
        serializer = CourseSerializer(data=request.data, many=True)

        if serializer.is_valid():
            courses_data = serializer.validated_data
            courses = [Course(**course_data) for course_data in courses_data]
            total_grade_points = sum(course.grade_point()*course.credit_units for course in courses)
            total_credit_units = sum(course.credit_units for course in courses)

            if total_credit_units == 0:  
                return Response({"error": "Total credit units cannot be zero"}, status=status.HTTP_400_BAD_REQUEST)
            
            cgpa = total_grade_points/total_credit_units
            print('works')
            # new
            user_lazy = SimpleLazyObject(lambda: self.request.user)
            user_pk = user_lazy.pk
            print(self.request.user)
            cgpa_saved_data = {'user_pk':user_pk, 'cgpa':cgpa}
            print(cgpa)
            cgpa_saved_serializer = CourseSerializer(data = cgpa_saved_data)
            print('move on')

            if cgpa_saved_serializer.is_valid():
                cgpa_saved_serializer.save()
                print('saved')
                return Response({'cgpa':cgpa, 'saved':True}, status=status.HTTP_200_OK)
            else:
                return Response(cgpa_saved_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            # new
            # return Response({"cgpa":cgpa}, status=status. HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



