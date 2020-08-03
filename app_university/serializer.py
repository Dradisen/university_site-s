from rest_framework import serializers
from app_university.models import *

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = "__all__"

class CathedraSerializer(serializers.ModelSerializer):
    header_cathedra = EmployeeSerializer(read_only=True)
    
    class Meta:
        model = Cathedra
        fields = "__all__"

class FacultySerializer(serializers.ModelSerializer):
    header_faculty = EmployeeSerializer(read_only=True)
    cathedra = CathedraSerializer(many=True)
    
    class Meta:
        model = Faculty
        fields = "__all__"

class RectorateSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(many=True)

    class Meta:
        model = RectoratePosition
        fields = "__all__"

