from django.urls import path
from app_university.views import *

urlpatterns = [
    path("", RectorateAPIView.as_view()),
    path("faculty/", FacultyAPIView.as_view()),
    path("employees/", EmployeeAPIView.as_view())
]
