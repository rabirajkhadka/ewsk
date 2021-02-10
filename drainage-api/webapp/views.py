from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Average, DataSet, Station
from .serializers import averageSerializer
from datetime import datetime, timedelta
from django.db.models import Avg
from decimal import Decimal


class webPages:

    def homepage(request):
        return render(request, 'home.html')


class averageList(APIView):

    def updateAverageData(self):

        Average.objects.all().delete()  # delete previous records
        # Finding the time
        today = datetime.now()
        oneHourTime = today - timedelta(hours=1)
        threeHourTime = today - timedelta(hours=3)
        sixHourTime = today - timedelta(hours=6)
        nineHourTime = today - timedelta(hours=9)
        twelveHourTime = today - timedelta(hours=12)
        oneDayTime = today - timedelta(days=1)
        oneWeekTime = today - timedelta(days=7)
        twoWeekTime = today - timedelta(days=14)
        threeWeekTime = today - timedelta(days=21)
        fourWeekTime = today - timedelta(days=28)
        aID = 1
        for data in Station.objects.all():

            # storing all time data and average to list
            dataList = []
            oneHourData = DataSet.objects.filter(station__exact=data.stationID).filter(
                dateTime__gt=oneHourTime).aggregate(Avg('drainageLevel'))
            dataList.insert(0, oneHourData)
            threeHourData = DataSet.objects.filter(station__exact=data.stationID).filter(
                dateTime__gt=threeHourTime).aggregate(Avg('drainageLevel'))
            dataList.insert(1, threeHourData)
            sixHourData = DataSet.objects.filter(station__exact=data.stationID).filter(
                dateTime__gt=sixHourTime).aggregate(Avg('drainageLevel'))
            dataList.insert(2, sixHourData)
            nineHourData = DataSet.objects.filter(station__exact=data.stationID).filter(
                dateTime__gt=nineHourTime).aggregate(Avg('drainageLevel'))
            dataList.insert(3, nineHourData)
            twelveHourData = DataSet.objects.filter(station__exact=data.stationID).filter(
                dateTime__gt=twelveHourTime).aggregate(Avg('drainageLevel'))
            dataList.insert(4, twelveHourData)
            oneDayData = DataSet.objects.filter(station__exact=data.stationID).filter(
                dateTime__gt=oneDayTime).aggregate(Avg('drainageLevel'))
            dataList.insert(5, oneDayData)
            oneWeekData = DataSet.objects.filter(station__exact=data.stationID).filter(
                dateTime__gt=oneWeekTime).aggregate(Avg('drainageLevel'))
            dataList.insert(6, oneWeekData)
            twoWeekData = DataSet.objects.filter(station__exact=data.stationID).filter(
                dateTime__gt=twoWeekTime).filter(station__exact=data.stationID).aggregate(Avg('drainageLevel'))
            dataList.insert(7, twoWeekData)
            threeWeekData = DataSet.objects.filter(station__exact=data.stationID).filter(
                dateTime__gt=threeWeekTime).aggregate(Avg('drainageLevel'))
            dataList.insert(8, threeWeekData)
            fourWeekData = DataSet.objects.filter(station__exact=data.stationID).filter(
                dateTime__gt=fourWeekTime).aggregate(Avg('drainageLevel'))
            dataList.insert(9, fourWeekData)

            # replacing invalid values to 0
            for count in range(10):
                if dataList[count]['drainageLevel__avg'] == None:
                    dataList[count]['drainageLevel__avg'] = Decimal("0.0")

            self.model = Average.objects.create(
                averageID="A"+str(aID),
                station=data,
                oneHour=dataList[0]['drainageLevel__avg'],
                threeHour=dataList[1]['drainageLevel__avg'],
                sixHour=dataList[2]['drainageLevel__avg'],
                nineHour=dataList[3]['drainageLevel__avg'],
                twelveHour=dataList[4]['drainageLevel__avg'],
                oneDay=dataList[5]['drainageLevel__avg'],
                oneWeek=dataList[6]['drainageLevel__avg'],
                twoWeek=dataList[7]['drainageLevel__avg'],
                threeWeek=dataList[8]['drainageLevel__avg'],
                fourWeek=dataList[9]['drainageLevel__avg'])
            aID += 1

    def get(self, request):
        self.updateAverageData()
        data = Average.objects.all()
        serializer = averageSerializer(data, many=True)
        return Response(serializer.data)

    def post(self):
        pass
