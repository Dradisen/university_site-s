from django.urls import path, re_path
from app_university.views import *

urlpatterns = [
    #Пункт 3) задача b
    re_path(r'(?P<structure>faculty|cathedra|rectorate)/employees/$', StructureEmployeeAPIView.as_view()),
    #Пункт 3) задача a
    re_path(r'(?P<structure>faculty|cathedra|rectorate)/$', StructureUniversityAPIView.as_view()),
    #Пункт 3) задача c
    path("employees/<int:id>/subheads/", EmployeeSubheadsAPIView.as_view()),
    #Пункт 3) задача d
    path("employees/<int:id>", EmployeeAPIView.as_view()),
    path("employees/", EmployeeAPIView.as_view()),
    path("", StructureUniversityAPIView.as_view()),
]
