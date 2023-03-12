from rest_framework import serializers
from .models import CurdModel

class Apiser(serializers.ModelSerializer):
    class Meta:
        model=CurdModel
        fields='__all__'

