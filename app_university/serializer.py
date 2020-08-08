from rest_framework import serializers
from app_university.models import *


#Сериализатор модели сотрудника
class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeModel
        fields = ['id', 'name', 'surname', 'last_name']

#Сериализатор модели сотрудника с расширенными полями
class EmployeeFullSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField('getPosition')

    def getPosition(self, data):
        if data.fk_position:
            position = FacultyPosition.objects.get(id=data.fk_position.id)
            return position.position_title

    class Meta:
        model = EmployeeModel
        fields = ["id", "surname","name","last_name", "birthday", "photo", "position"]


#Сериализатор модели кафедры
class CathedraSerializer(serializers.ModelSerializer):
    header_cathedra = EmployeeSerializer(read_only=True)
    class Meta:
        model = CathedraModel
        fields = ['id', 'header_cathedra', 'name_cathedra']

#Сериализатор модели кафедры со связанными данными сотрудника
class CathedraEmployeeSerializer(serializers.ModelSerializer):
    header_cathedra = EmployeeFullSerializer(read_only=True)
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = CathedraModel
        fields = ['name_cathedra', 'header_cathedra', 'employees']

#Сериализатор модели факультета
class FacultySerializer(serializers.ModelSerializer):
    header_faculty = EmployeeSerializer(read_only=True)
    cathedra = CathedraSerializer(many=True)
 
    class Meta:
        model = FacultyModel
        fields = ['id', 'header_faculty', 'name_faculty', 'cathedra']

#Сериализатор модели факультета со связанными данными сотрудника
class FacultyEmployeeSerializer(serializers.ModelSerializer):
    header_faculty = EmployeeFullSerializer(read_only=True)

    class Meta:
        model = FacultyModel
        fields = ['name_faculty', 'header_faculty']

#Сериализатор модели ректората
class RectorateSerializer(serializers.ModelSerializer):
    header_rectorate = EmployeeSerializer()
    leads = FacultySerializer(many=True)

    class Meta:
        model = RectorateModel
        fields = ['id', 'header_rectorate', 'position_title', 'leads']

#Сериализатор модели ректората со связанными данными сотрудника
class RectorateEmployeeSerializer(serializers.ModelSerializer):
    header_rectorate = EmployeeFullSerializer()

    class Meta:
        model = RectorateModel
        fields = ['position_title', 'header_rectorate']