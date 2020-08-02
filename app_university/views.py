from django.shortcuts import render
from rest_framework import generic
from app_university.serializer import IndexSerializer


class IndexView(generic.CreateAPIView):
    serializer_class = IndexSerializer
