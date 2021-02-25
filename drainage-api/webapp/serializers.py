from rest_framework import serializers
from .models import Average, DataSet, Station, DrainageTrend


class averageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Average
        fields = '__all__'


class dataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSet
        fields = '__all__'


class stationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['stationID']


class trendSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrainageTrend
        fields = '__all__'
