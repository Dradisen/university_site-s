from django.shortcuts import render
from rest_framework import generics
from app_university.serializer import *
from app_university.models import *


# class RectorateAPIView(generics.ListAPIView):
#     #queryset = RectoratePosition.objects.all() 
#     serializer_class = RectorateSerializer
#     fields = ['id', 'position_title', 'leads', 'belong_id']

#     def get_queryset(self):
#         order_values = self.request.GET.getlist('order')

#         if(len(order_values)):
#             for i, item in enumerate(order_values):
#                 if not ((item[0] == "-" and item[1:] in self.fields) or (item in self.fields)):
#                     del order_values[i]
                    
#             return RectoratePosition.objects.all().order_by(*order_values)
#         return RectoratePosition.objects.all()

class FacultyAPIView(generics.ListAPIView):
    queryset = Faculty.objects.all() 
    serializer_class = FacultySerializer


class StructureUniversityAPIView(generics.ListAPIView):
    queryset = RectoratePosition.objects.all()
    serializer_class = RectorateSerializer

    def get_queryset(self):
        order_values = self.request.GET.getlist('order')

        if ('structure' in self.kwargs):
            structure = self.kwargs['structure']

            if(structure == 'rectorate'):
                filters = ['id', 'position_title', 'leads', 'belong_id']
                self.serializer_class = RectorateSerializer
                model = RectoratePosition
            elif(structure == 'faculty'):
                filters = ['id', 'header_faculty', 'name_faculty', 'cathedra', 'slug']
                self.serializer_class = FacultySerializer
                model = Faculty
            elif(structure == 'cathedra'):
                filters = ['id', 'header_cathedra', 'name_cathedra', 'slug', 'employees']
                self.serializer_class = CathedraSerializer
                model = Cathedra
    
            if(len(order_values)):
                for i, item in enumerate(order_values):
                    if not ((item[0] == "-" and item[1:] in filters) or (item in filters)):
                        del order_values[i]

                return model.objects.all().order_by(*order_values)
            return model.objects.all()

        return RectoratePosition.objects.all()



class EmployeeAPIView(generics.ListAPIView):
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

        if ('structure' in self.kwargs):
            structure = self.kwargs['structure']

            if(structure == 'rectorate'):
                self.serializer_class = RectorateEmployeeSerializer
                return RectoratePosition.objects.filter(header_rectorate__isnull=False)
            elif(structure == 'faculty'):
                self.serializer_class = EmployeeSerializer
                return Employee.objects.filter(fk_faculties__isnull=False)
            elif(structure == 'cathedra'):
                self.serializer_class = EmployeeSerializer
                return Employee.objects.filter(fk_cathedra__isnull=False)

            return Employee.objects.all()
        return Employee.objects.all()