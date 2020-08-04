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
    #queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        if 'id' in self.kwargs:
            ids = int(self.kwargs['id'])

            if(ids):
                return Employee.objects.all().filter(id=ids)
        return Employee.objects.all()



class StructureEmployeeAPIView(generics.ListAPIView):
    #queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        #print(self.kwargs['structure'])
        if ('structure' in self.kwargs):
            structure = self.kwargs['structure']

            if(structure == 'rectorate'):
                self.serializer_class = RectorateEmployeeSerializer
                return RectoratePosition.objects.filter(header_rectorate__isnull=False)
            elif(structure == 'faculty'):
                self.serializer_class = FacultyEmployeeSerializer
                return Faculty.objects.filter(header_faculty__isnull=False)
            elif(structure == 'cathedra'):
                self.serializer_class = CathedraEmployeeSerializer
                return Cathedra.objects.all()

            return Employee.objects.all()
        return Employee.objects.all()