from rest_framework import serializers
from app_university.models import *

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

class CathedraSerializer(serializers.ModelSerializer):
    header_cathedra = EmployeeSerializer(read_only=True)
    employees = EmployeeSerializer(many=True)
    class Meta:
        model = Cathedra
        fields = "__all__"

class CathedraEmployeeSerializer(serializers.ModelSerializer):
    header_cathedra = EmployeeSerializer(read_only=True)
    employees = EmployeeSerializer(many=True)
    
    class Meta:
        model = Cathedra
        fields = ['name_cathedra', 'header_cathedra', 'employees']

class FacultySerializer(serializers.ModelSerializer):
    header_faculty = EmployeeSerializer(read_only=True)
    cathedra = CathedraSerializer(many=True)

    class Meta:
        model = Faculty
        fields = "__all__"

class FacultyEmployeeSerializer(serializers.ModelSerializer):
    header_faculty = EmployeeSerializer(read_only=True)

    class Meta:
        model = Faculty
        fields = ['name_faculty', 'header_faculty']

class RectorateSerializer(serializers.ModelSerializer):
    header_rectorate = EmployeeSerializer(read_only=True)
    leads = FacultySerializer(many=True)

    class Meta:
        model = RectoratePosition
        fields = "__all__"

class RectorateEmployeeSerializer(serializers.ModelSerializer):
    header_rectorate = EmployeeSerializer(read_only=True)

    class Meta:
        model = RectoratePosition
        fields = ['position_title', 'header_rectorate']