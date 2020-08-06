from django.urls import path, re_path
from app_university.views import *

urlpatterns = [
    re_path(r'(?P<structure>faculty|cathedra|rectorate)/employees/$', StructureEmployeeAPIView.as_view()),
    re_path(r'(?P<structure>faculty|cathedra|rectorate)/$', StructureUniversityAPIView.as_view()),
    path("employees/<int:id>/subheads/", EmployeeSubheadsAPIView.as_view()),
    path("employees/<int:id>", EmployeeAPIView.as_view()),
    path("employees/", EmployeeAPIView.as_view()),
    path("", StructureUniversityAPIView.as_view()),
]
