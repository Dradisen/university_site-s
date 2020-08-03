from django.shortcuts import render
from rest_framework import generics
from app_university.serializer import *
from app_university.models import *


class RectorateAPIView(generics.ListAPIView):
    queryset = RectoratePosition.objects.all() 
    serializer_class = RectorateSerializer


class FacultyAPIView(generics.ListAPIView):
    queryset = Faculty.objects.all() 
    serializer_class = FacultySerializer

class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer