from django.urls import path, re_path
from app_university.views import *

urlpatterns = [
    #Пункт 3) задача b
    #Получение списка cотрудников подразделения
    re_path(r'(?P<structure>faculty|cathedra|rectorate)/employees/$', StructureEmployeeAPIView.as_view()),
    #Пункт 3) задача a
    #Получение списка подразделений с дочерними подразделениями и возможностью сортировки по ключу order=[id, header_*, name_* ]
    re_path(r'(?P<structure>faculty|cathedra|rectorate)/$', StructureUniversityAPIView.as_view()),
    #Пункт 3) задача c
    #Получение подчинённых сотрудников от конкретного человека(если есть)
    path("employees/<int:id>/subheads/", EmployeeSubheadsAPIView.as_view()),
    #Пункт 3) задача d
    #Получение сведений сотрудника
    path("employees/<int:id>", EmployeeAPIView.as_view()),
    path("employees/", EmployeeAPIView.as_view()),
    path("", StructureUniversityAPIView.as_view()),
]
