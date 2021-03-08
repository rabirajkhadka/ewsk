from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Average, DataSet, Station, DrainageTrend
from .serializers import averageSerializer, dataSetSerializer, stationSerializer, trendSerializer
from datetime import datetime, timedelta


class dataSetList(APIView):

    def get(self, request):
        data = DataSet.objects.all().order_by('-dateTime')
        serializer = dataSetSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = dataSetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class stationList(APIView):

    def get(self, request):
        data = Station.objects.all()
        serializer = stationSerializer(data, many=True)
        return Response(serializer.data)


def homePage(request):
    return render(request, 'home.html')


def dataPage(request):
    return render(request, 'data.html')


class averageList(APIView):

    def get(self, request, stationID):

        today = datetime.now()
        oneHourTime = today - timedelta(hours=1)
        data = Average.objects.all().filter(
            station__exact=stationID).filter(dateTime__range=(oneHourTime, today)).order_by('-dateTime')
        serializer = averageSerializer(data, many=True)
        return Response(serializer.data)


class dataSetStation(APIView):

    def get(self, request, stationID):

        today = datetime.now()
        oneHourTime = today - timedelta(hours=1)
        # filter(dateTime__range = (oneHourTime, today)).
        data = DataSet.objects.all().filter(
            station__exact=stationID).filter(dateTime__range=(oneHourTime, today)).order_by('-dateTime')

        serializer = dataSetSerializer(data, many=True)
        return Response(serializer.data)


class trendList(APIView):

    def get(self, request, stationID):

        data = DrainageTrend.objects.all().filter(
            station__exact=stationID).order_by('-dateTime')

        serializer = trendSerializer(data, many=True)
        return Response(serializer.data)
