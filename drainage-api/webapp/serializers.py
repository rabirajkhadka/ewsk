from rest_framework import serializers
from .models import Average


class averageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Average
        fields = '__all__'
