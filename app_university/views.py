from django.shortcuts import render
from rest_framework import generics
from app_university.serializer import *
from app_university.models import *


class RectorateAPIView(generics.ListAPIView):
    #queryset = RectoratePosition.objects.all() 
    serializer_class = RectorateSerializer
    fields = ['id', 'position_title', 'faculty', 'belong_id']

    def get_queryset(self):
        order_values = self.request.GET.getlist('order')
        
        if(len(order_values)):
            for i, item in enumerate(order_values):
                print(item[1:])
                if not ((item[0] == "-" and item[1:] in self.fields) or (item in self.fields)):
                    del order_values[i]
                    
            return RectoratePosition.objects.all().order_by(*order_values)

        return RectoratePosition.objects.all()

class FacultyAPIView(generics.ListAPIView):
    queryset = Faculty.objects.all() 
    serializer_class = FacultySerializer

class EmployeeAPIView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer