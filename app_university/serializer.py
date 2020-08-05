from rest_framework import serializers
from app_university.models import *

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'last_name']

class EmployeeFullSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField('getPosition')

    def getPosition(self, data):
        if data.fk_position:
            position = FacultyPosition.objects.get(id=data.fk_position.id)
            return position.position_title

    class Meta:
        model = Employee
        fields = ["id", "surname","name","last_name", "birthday", "photo", "position"]
    



class CathedraSerializer(serializers.ModelSerializer):
    header_cathedra = EmployeeSerializer(read_only=True)
    #employees = EmployeeSerializer(many=True)
    # header_cathedra = serializers.SerializerMethodField('getNameEmployee')

    # def getNameEmployee(self, data):
    #     if data.header_cathedra is not None:
    #         header = Employee.objects.get(id=data.header_cathedra)
    #         return "{} {} {}".format(header.surname, header.name, header.last_name)
    class Meta:
        model = Cathedra
        fields = ['id', 'header_cathedra', 'name_cathedra']

class CathedraEmployeeSerializer(serializers.ModelSerializer):
    header_cathedra = EmployeeFullSerializer(read_only=True)
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = Cathedra
        fields = ['name_cathedra', 'header_cathedra', 'employees']

class FacultySerializer(serializers.ModelSerializer):
    header_faculty = EmployeeSerializer(read_only=True)
    cathedra = CathedraSerializer(many=True)
    # header_faculty = serializers.SerializerMethodField('getNameEmployee')

    # def getNameEmployee(self, data):
    #     if data.header_faculty is not None:
    #         header = Employee.objects.get(id=data.header_faculty)
    #         return "{} {} {}".format(header.surname, header.name, header.last_name)
    class Meta:
        model = Faculty
        fields = ['id', 'header_faculty', 'name_faculty', 'cathedra']

class FacultyEmployeeSerializer(serializers.ModelSerializer):
    header_faculty = EmployeeFullSerializer(read_only=True)

    class Meta:
        model = Faculty
        fields = ['name_faculty', 'header_faculty']

class RectorateSerializer(serializers.ModelSerializer):
    header_rectorate = EmployeeSerializer()
    leads = FacultySerializer(many=True)
    # header_rectorate = serializers.SerializerMethodField('getNameEmployee')

    # def getNameEmployee(self, data):
    #     if data.header_rectorate is not None:
    #         header = Employee.objects.get(id=data.header_rectorate)
    #         return "{} {} {}".format(header.surname, header.name, header.last_name)


    class Meta:
        model = RectoratePosition
        fields = ['id', 'header_rectorate', 'position_title', 'leads']

class RectorateEmployeeSerializer(serializers.ModelSerializer):
    header_rectorate = EmployeeFullSerializer()
    # header_rectorate = serializers.SerializerMethodField('getNameEmployee')

    # def getNameEmployee(self, data):
    #     if data.header_rectorate is not None:
    #         header = Employee.objects.get(id=data.header_rectorate)
    #         return EmployeeFullSerializer(header).data

    class Meta:
        model = RectoratePosition
        fields = ['position_title', 'header_rectorate']