from rest_framework import serializers
from app_university.models import *

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = RectoratePosition
        fields = "__all__"