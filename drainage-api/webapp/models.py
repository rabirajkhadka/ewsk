from django.db import models
from datetime import datetime, timedelta
from django.db.models import Avg
from decimal import Decimal


class Station(models.Model):
    stationID = models.CharField(primary_key=True, max_length=5)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class DataSet(models.Model):
    datasetID = models.CharField(primary_key=True, max_length=5)
    station = models.ForeignKey(
        Station, default=1, on_delete=models.SET_DEFAULT)
    dateTime = models.DateTimeField(auto_now_add=True)
    dateTime.editable = True
    drainageLevel = models.DecimalField(max_digits=10, decimal_places=3)
    delayTime = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return str(self.dateTime)

    def save(self, *args, **kwargs):
        ###
        super().save(*args, **kwargs)
        # run code whenever saved
        # Average.objects.all().delete()  # delete previous records

        # # Finding the time
        # today = datetime.now()
        # oneHourTime = today - timedelta(hours=1)
        # threeHourTime = today - timedelta(hours=3)
        # sixHourTime = today - timedelta(hours=6)
        # nineHourTime = today - timedelta(hours=9)
        # twelveHourTime = today - timedelta(hours=12)
        # oneDayTime = today - timedelta(days=1)
        # oneWeekTime = today - timedelta(days=7)
        # twoWeekTime = today - timedelta(days=14)
        # threeWeekTime = today - timedelta(days=21)
        # fourWeekTime = today - timedelta(days=28)

        # # storing all time data and average to list
        # dataList = []

        # oneHourData = DataSet.objects.filter(
        #     dateTime__gt=oneHourTime).aggregate(Avg('drainageLevel'))
        # dataList.insert(0, oneHourData)
        # threeHourData = DataSet.objects.filter(
        #     dateTime__gt=threeHourTime).aggregate(Avg('drainageLevel'))
        # dataList.insert(1, threeHourData)
        # sixHourData = DataSet.objects.filter(
        #     dateTime__gt=sixHourTime).aggregate(Avg('drainageLevel'))
        # dataList.insert(2, sixHourData)
        # nineHourData = DataSet.objects.filter(
        #     dateTime__gt=nineHourTime).aggregate(Avg('drainageLevel'))
        # dataList.insert(3, nineHourData)
        # twelveHourData = DataSet.objects.filter(
        #     dateTime__gt=twelveHourTime).aggregate(Avg('drainageLevel'))
        # dataList.insert(4, twelveHourData)
        # oneDayData = DataSet.objects.filter(
        #     dateTime__gt=oneDayTime).aggregate(Avg('drainageLevel'))
        # dataList.insert(5, oneDayData)
        # oneWeekData = DataSet.objects.filter(
        #     dateTime__gt=oneWeekTime).aggregate(Avg('drainageLevel'))
        # dataList.insert(6, oneWeekData)
        # twoWeekData = DataSet.objects.filter(
        #     dateTime__gt=twoWeekTime).aggregate(Avg('drainageLevel'))
        # dataList.insert(7, twoWeekData)
        # threeWeekData = DataSet.objects.filter(
        #     dateTime__gt=threeWeekTime).aggregate(Avg('drainageLevel'))
        # dataList.insert(8, threeWeekData)
        # fourWeekData = DataSet.objects.filter(
        #     dateTime__gt=fourWeekTime).aggregate(Avg('drainageLevel'))
        # dataList.insert(9, fourWeekData)

        # # replacing invalid values to 0
        # for count in range(10):
        #     if dataList[count]['drainageLevel__avg'] == None:
        #         dataList[count]['drainageLevel__avg'] = Decimal("0.0")

        # self.model = Average.objects.create(
        #     averageID="A1",
        #     station=self.station,
        #     oneHour=dataList[0]['drainageLevel__avg'],
        #     threeHour=dataList[1]['drainageLevel__avg'],
        #     sixHour=dataList[2]['drainageLevel__avg'],
        #     nineHour=dataList[3]['drainageLevel__avg'],
        #     twelveHour=dataList[4]['drainageLevel__avg'],
        #     oneDay=dataList[5]['drainageLevel__avg'],
        #     oneWeek=dataList[6]['drainageLevel__avg'],
        #     twoWeek=dataList[7]['drainageLevel__avg'],
        #     threeWeek=dataList[8]['drainageLevel__avg'],
        #     fourWeek=dataList[9]['drainageLevel__avg'])


class Average(models.Model):
    averageID = models.CharField(primary_key=True, max_length=5)
    station = models.ForeignKey(
        Station, default=1, on_delete=models.SET_DEFAULT)
    oneHour = models.DecimalField(max_digits=10, decimal_places=3)
    threeHour = models.DecimalField(max_digits=10, decimal_places=3)
    sixHour = models.DecimalField(max_digits=10, decimal_places=3)
    nineHour = models.DecimalField(max_digits=10, decimal_places=3)
    twelveHour = models.DecimalField(max_digits=10, decimal_places=3)
    oneDay = models.DecimalField(max_digits=10, decimal_places=3)
    oneWeek = models.DecimalField(max_digits=10, decimal_places=3)
    twoWeek = models.DecimalField(max_digits=10, decimal_places=3)
    threeWeek = models.DecimalField(max_digits=10, decimal_places=3)
    fourWeek = models.DecimalField(max_digits=10, decimal_places=3)
    dateTime = models.DateTimeField(
        auto_now_add=True)

    def __str__(self):
        return self.station.name


class DrainageTrend(models.Model):
    trendID = models.CharField(primary_key=True, max_length=5)
    station = models.ForeignKey(
        Station, default=1, on_delete=models.SET_DEFAULT)
    trendValue = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.station.name


class WarningMessageData(models.Model):
    warningID = models.CharField(primary_key=True, max_length=5)
    threshold = models.CharField(max_length=10)
    season = models.CharField(max_length=15)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.warningID


class WarningMessage(models.Model):
    messageID = models.CharField(primary_key=True, max_length=5)
    station = models.ForeignKey(
        Station, default=1, on_delete=models.SET_DEFAULT)
    warningValue = models.ForeignKey(
        WarningMessageData, default=1, on_delete=models.SET_DEFAULT)
    dateTime = dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.station.name
