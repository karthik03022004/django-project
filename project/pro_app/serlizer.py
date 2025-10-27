from rest_framework import serializers
from .models import Employee
class Empserlizer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"