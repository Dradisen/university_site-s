from django.urls import path, re_path
from app_university.views import *

urlpatterns = [
    re_path(r'(?P<structure>faculty|cathedra|rectorate)/employees/$', StructureEmployeeAPIView.as_view()),
    #path("faculty/", FacultyAPIView.as_view()),
    path("employees/<int:id>", EmployeeAPIView.as_view()),
    path("employees/", EmployeeAPIView.as_view()),
    path("", RectorateAPIView.as_view()),
]
