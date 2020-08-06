from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from django.db.models.query import QuerySet
from rest_framework import generics
from rest_framework.response import Response
from app_university.serializer import *
from app_university.models import *

class FacultyAPIView(generics.ListAPIView):
    queryset = FacultyModel.objects.all() 
    serializer_class = FacultySerializer

class StructureUniversityAPIView(generics.ListAPIView):
    queryset = RectorateModel.objects.all()
    serializer_class = RectorateSerializer

    def get_queryset(self):
        order_values = self.request.GET.getlist('order')

        if ('structure' in self.kwargs):
            structure = self.kwargs['structure']

            if(structure == 'rectorate'):
                filters = ['id', 'position_title', 'leads']
                self.serializer_class = RectorateSerializer
                model = RectorateModel
            elif(structure == 'faculty'):
                filters = ['id', 'header_faculty', 'name_faculty']
                self.serializer_class = FacultySerializer
                model = FacultyModel
            elif(structure == 'cathedra'):
                filters = ['id', 'header_cathedra', 'name_cathedra']
                self.serializer_class = CathedraSerializer
                model = CathedraModel
    
            if(len(order_values)):
                for i, item in enumerate(order_values):
                    if not ((item[0] == "-" and item[1:] in filters) or (item in filters)):
                        del order_values[i]

                return model.objects.all().order_by(*order_values)
            return model.objects.all()

        return RectorateModel.objects.all()



class EmployeeAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        if 'id' in self.kwargs:
            ids = int(self.kwargs['id'])

            if(ids):
                return EmployeeModel.objects.all().filter(id=ids)
        return EmployeeModel.objects.all()



class EmployeeSubheadsAPIView(generics.ListAPIView):
    serializer_class = EmployeeFullSerializer

    def get_queryset(self):
        id_employee = self.kwargs['id']

        if not id_employee is None:
            employee = get_object_or_404(EmployeeModel, id=id_employee)

            if not employee.rectorate_position  is None:
                rectorate_employees = RectorateModel.objects.prefetch_related().filter(belong_id=employee.rectorate.id, header_rectorate__isnull=False)
                faculty_employees = FacultyModel.objects.prefetch_related().filter(belong_rectorate=employee.rectorate.id, header_faculty__isnull=False)
                ids_employees = []
                for item in rectorate_employees:
                    ids_employees.append(item.header_rectorate.id)

                for item in faculty_employees:
                    ids_employees.append(item.header_faculty.id)

                return EmployeeModel.objects.filter(id__in=ids_employees)

            elif not employee.faculty_position is None:
                return EmployeeModel.objects.filter(fk_faculties=employee.faculty.id, cathedra_position__isnull=False)
            elif not employee.cathedra_position is None:
                return EmployeeModel.objects.filter(fk_cathedra=employee.cathedra.id).exclude(id=id_employee)
            else:
                return EmployeeModel.objects.filter(id__isnull=True)

class StructureEmployeeAPIView(generics.ListAPIView):
    #queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filters = ['name', 'surname', 'last_name']

    def get_queryset(self):
        order_values = self.request.GET.getlist('order')
        
        if ('structure' in self.kwargs):
            structure = self.kwargs['structure']

            if(len(order_values)):
                for i, item in enumerate(order_values):
                    if (item[0] == "-" and item[1:] in self.filters):
                        order_values[i] = "-header_"+self.kwargs['structure']+"__"+item[1:]
                    elif (item in self.filters):
                        order_values[i] = "header_"+self.kwargs['structure']+"__"+item
                    else:
                        del order_values[i]

            if(structure == 'rectorate'):
                self.serializer_class = RectorateEmployeeSerializer
                return RectorateModel.objects.filter(header_rectorate__isnull=False).order_by(*order_values)
            elif(structure == 'faculty'):
                self.serializer_class = FacultyEmployeeSerializer
                return FacultyModel.objects.filter(header_faculty__isnull=False).order_by(*order_values)
            elif(structure == 'cathedra'):
                self.serializer_class = CathedraEmployeeSerializer
                return CathedraModel.objects.all().order_by(*order_values)