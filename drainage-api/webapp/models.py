from django.db import models
from datetime import datetime, timedelta
from django.db.models import Avg
from decimal import Decimal
import numpy as np
import pandas as pd  # To read data
import matplotlib.dates as mdates
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Station(models.Model):
    stationID = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    communityHero1 = models.CharField(
        max_length=255, default='John Doe, 980XXXXXX')
    communityHero2 = models.CharField(
        max_length=255, default='John Doe, 980XXXXXX')

    def __str__(self):
        return self.name


class DataSet(models.Model):

    station = models.ForeignKey(
        Station, default='S1', on_delete=models.SET_DEFAULT)
    dateTime = models.DateTimeField(default=timezone.now)
    dateTime.editable = False  # to edit dates to try
    drainageLevel = models.DecimalField(max_digits=100, decimal_places=3)
    delayTime = models.DecimalField(max_digits=100, decimal_places=3)

    def __str__(self):
        return str(self.station) + ' ' + str(self.dateTime)

    # def save(self, *args, **kwargs):
        # super().save(*args, **kwargs)
        # # Average Calculations
        # stationData = self.station
        # # getting station ID
        # for oneSetData in Station.objects.all():
        #     if str(stationData) == str(oneSetData.name):
        #         stationData = oneSetData.stationID
        #         break
        # # Average.objects.all().delete()  # use this to refresh data
        # aID = 1
        # today = self.dateTime
        # print(self.drainageLevel)
        # print(self.delayTime)
        # print(today)
        # print(today)
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

        # # for data in Station.objects.all():
        # print(self.station_id)
        # # storing all time data and average to list
        # dataList = []
        # oneHourData = DataSet.objects.filter(station__exact=self.station_id).filter(
        #     dateTime__range=(oneHourTime, today)).aggregate(Avg('drainageLevel'))
        # dataList.insert(0, oneHourData)
        # threeHourData = DataSet.objects.filter(station__exact=self.station_id).filter(
        #     dateTime__range=(threeHourTime, today)).aggregate(Avg('drainageLevel'))
        # dataList.insert(1, threeHourData)
        # sixHourData = DataSet.objects.filter(station__exact=self.station_id).filter(
        #     dateTime__range=(sixHourTime, today)).aggregate(Avg('drainageLevel'))
        # dataList.insert(2, sixHourData)
        # nineHourData = DataSet.objects.filter(station__exact=self.station_id).filter(
        #     dateTime__range=(nineHourTime, today)).aggregate(Avg('drainageLevel'))
        # dataList.insert(3, nineHourData)
        # twelveHourData = DataSet.objects.filter(station__exact=self.station_id).filter(
        #     dateTime__range=(twelveHourTime, today)).aggregate(Avg('drainageLevel'))
        # dataList.insert(4, twelveHourData)
        # oneDayData = DataSet.objects.filter(station__exact=self.station_id).filter(
        #     dateTime__range=(oneDayTime, today)).aggregate(Avg('drainageLevel'))
        # dataList.insert(5, oneDayData)
        # oneWeekData = DataSet.objects.filter(station__exact=self.station_id).filter(
        #     dateTime__range=(oneWeekTime, today)).aggregate(Avg('drainageLevel'))
        # dataList.insert(6, oneWeekData)
        # twoWeekData = DataSet.objects.filter(station__exact=self.station_id).filter(
        #     dateTime__range=(twoWeekTime, today)).aggregate(Avg('drainageLevel'))
        # dataList.insert(7, twoWeekData)
        # threeWeekData = DataSet.objects.filter(station__exact=self.station_id).filter(
        #     dateTime__range=(threeWeekTime, today)).aggregate(Avg('drainageLevel'))
        # dataList.insert(8, threeWeekData)
        # fourWeekData = DataSet.objects.filter(station__exact=self.station_id).filter(
        #     dateTime__range=(fourWeekTime, today)).aggregate(Avg('drainageLevel'))
        # dataList.insert(9, fourWeekData)

        # # replacing invalid values to 0
        # for count in range(10):
        #     if dataList[count]['drainageLevel__avg'] == None:
        #         dataList[count]['drainageLevel__avg'] = Decimal("0.0")

        # # for averageDataSet in Average.objects.all():
        # #     if int(averageDataSet.averageID[1:]) >= aID:
        # #         aID = int(averageDataSet.averageID[1:])+1

        # self.model = Average.objects.create(
        #     # averageID="A"+str(aID),
        #     station=self.station,  # need to change
        #     oneHour=dataList[0]['drainageLevel__avg'],
        #     threeHour=dataList[1]['drainageLevel__avg'],
        #     sixHour=dataList[2]['drainageLevel__avg'],
        #     nineHour=dataList[3]['drainageLevel__avg'],
        #     twelveHour=dataList[4]['drainageLevel__avg'],
        #     oneDay=dataList[5]['drainageLevel__avg'],
        #     oneWeek=dataList[6]['drainageLevel__avg'],
        #     twoWeek=dataList[7]['drainageLevel__avg'],
        #     threeWeek=dataList[8]['drainageLevel__avg'],
        #     fourWeek=dataList[9]['drainageLevel__avg'],
        #     dateTime=today)

        # # trend Data
        # print('count', DataSet.objects.filter(station__exact=self.station_id).filter(
        #     dateTime__range=(oneHourTime, today)).count())
        # if DataSet.objects.filter(station__exact=self.station_id).filter(
        #         dateTime__range=(oneHourTime, today)).count() > 1:
        #     tID = 1
        #     data = pd.read_json(
        #         f'http://127.0.0.1:8000/api/datasetstation/{stationData}/?format=json')
        #     data = data.drop(columns=['id', 'delayTime', 'station'])
        #     # data.loc[len(data.index)] = [self.dateTime, self.drainageLevel]
        #     # print(data)
        #     # print(type(self.drainageLevel))
        #     x = mdates.date2num(data['dateTime'])
        #     # gets linear line values
        #     coefficients = np.polyfit(
        #         x, data['drainageLevel'], 1)  # m and c values
        #     print(type(data))
        #     m = round(coefficients[0], 3)
        #     c = round(coefficients[1], 3)
        #     print(m, c)

        #     self.model = DrainageTrend.objects.create(
        #         # trendID="T"+str(tID),
        #         station=self.station,  # need to change
        #         trendValue=m,
        #         yIntercept=c,
        #         dateTime=datetime.now())
        # super().save(*args, **kwargs)


def dataset_handler(sender, instance, **kwargs):
    # Average Calculations
    stationData = instance.station
    # getting station ID
    for oneSetData in Station.objects.all():
        if str(stationData) == str(oneSetData.name):
            stationData = oneSetData.stationID
            break
    # Average.objects.all().delete()  # use this to refresh data
    aID = 1
    today = instance.dateTime
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

    # for data in Station.objects.all():
    # storing all time data and average to list
    dataList = []
    oneHourData = DataSet.objects.filter(station__exact=instance.station_id).filter(
        dateTime__range=(oneHourTime, today)).aggregate(Avg('drainageLevel'))
    dataList.insert(0, oneHourData)
    threeHourData = DataSet.objects.filter(station__exact=instance.station_id).filter(
        dateTime__range=(threeHourTime, today)).aggregate(Avg('drainageLevel'))
    dataList.insert(1, threeHourData)
    sixHourData = DataSet.objects.filter(station__exact=instance.station_id).filter(
        dateTime__range=(sixHourTime, today)).aggregate(Avg('drainageLevel'))
    dataList.insert(2, sixHourData)
    nineHourData = DataSet.objects.filter(station__exact=instance.station_id).filter(
        dateTime__range=(nineHourTime, today)).aggregate(Avg('drainageLevel'))
    dataList.insert(3, nineHourData)
    twelveHourData = DataSet.objects.filter(station__exact=instance.station_id).filter(
        dateTime__range=(twelveHourTime, today)).aggregate(Avg('drainageLevel'))
    dataList.insert(4, twelveHourData)
    oneDayData = DataSet.objects.filter(station__exact=instance.station_id).filter(
        dateTime__range=(oneDayTime, today)).aggregate(Avg('drainageLevel'))
    dataList.insert(5, oneDayData)
    oneWeekData = DataSet.objects.filter(station__exact=instance.station_id).filter(
        dateTime__range=(oneWeekTime, today)).aggregate(Avg('drainageLevel'))
    dataList.insert(6, oneWeekData)
    twoWeekData = DataSet.objects.filter(station__exact=instance.station_id).filter(
        dateTime__range=(twoWeekTime, today)).aggregate(Avg('drainageLevel'))
    dataList.insert(7, twoWeekData)
    threeWeekData = DataSet.objects.filter(station__exact=instance.station_id).filter(
        dateTime__range=(threeWeekTime, today)).aggregate(Avg('drainageLevel'))
    dataList.insert(8, threeWeekData)
    fourWeekData = DataSet.objects.filter(station__exact=instance.station_id).filter(
        dateTime__range=(fourWeekTime, today)).aggregate(Avg('drainageLevel'))
    dataList.insert(9, fourWeekData)

    # replacing invalid values to 0
    for count in range(10):
        if dataList[count]['drainageLevel__avg'] == None:
            dataList[count]['drainageLevel__avg'] = Decimal("0.0")

    # for averageDataSet in Average.objects.all():
    #     if int(averageDataSet.averageID[1:]) >= aID:
    #         aID = int(averageDataSet.averageID[1:])+1

    Average.objects.create(
        # averageID="A"+str(aID),
        station=instance.station,  # need to change
        oneHour=dataList[0]['drainageLevel__avg'],
        threeHour=dataList[1]['drainageLevel__avg'],
        sixHour=dataList[2]['drainageLevel__avg'],
        nineHour=dataList[3]['drainageLevel__avg'],
        twelveHour=dataList[4]['drainageLevel__avg'],
        oneDay=dataList[5]['drainageLevel__avg'],
        oneWeek=dataList[6]['drainageLevel__avg'],
        twoWeek=dataList[7]['drainageLevel__avg'],
        threeWeek=dataList[8]['drainageLevel__avg'],
        fourWeek=dataList[9]['drainageLevel__avg'],
        dateTime=datetime.now())

    # trend Data
    print('count', DataSet.objects.filter(station__exact=instance.station_id).filter(
        dateTime__range=(oneHourTime, today)).count())

    if DataSet.objects.filter(station__exact=instance.station_id).filter(
            dateTime__range=(oneHourTime, today)).count() > 1:

        data = pd.DataFrame(list(DataSet.objects.filter(station__exact=instance.station_id).filter(
            dateTime__range=(oneHourTime, today)).values('drainageLevel', 'dateTime')))
        x = mdates.date2num(data['dateTime'])
        # gets linear line values
        coefficients = np.polyfit(
            x, data['drainageLevel'].astype(float), 1)  # m and c values
        m = round(coefficients[0], 3)
        c = round(coefficients[1], 3)
        print(m, c)

        DrainageTrend.objects.create(
            # trendID="T"+str(tID),
            station=instance.station,  # need to change
            trendValue=m,
            yIntercept=c,
            dateTime=datetime.now())


post_save.connect(dataset_handler, sender=DataSet)


class Average(models.Model):
    #averageID = models.CharField(primary_key=True, max_length=255)
    station = models.ForeignKey(
        Station, default=1, on_delete=models.SET_DEFAULT)
    oneHour = models.DecimalField(max_digits=100, decimal_places=3)
    threeHour = models.DecimalField(max_digits=100, decimal_places=3)
    sixHour = models.DecimalField(max_digits=100, decimal_places=3)
    nineHour = models.DecimalField(max_digits=100, decimal_places=3)
    twelveHour = models.DecimalField(max_digits=100, decimal_places=3)
    oneDay = models.DecimalField(max_digits=100, decimal_places=3)
    oneWeek = models.DecimalField(max_digits=100, decimal_places=3)
    twoWeek = models.DecimalField(max_digits=100, decimal_places=3)
    threeWeek = models.DecimalField(max_digits=100, decimal_places=3)
    fourWeek = models.DecimalField(max_digits=100, decimal_places=3)
    dateTime = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return str(self.station.name) + ' ' + str(self.dateTime)


class DrainageTrend(models.Model):
    #trendID = models.CharField(primary_key=True, max_length=255)
    station = models.ForeignKey(
        Station, default=1, on_delete=models.SET_DEFAULT)
    trendValue = models.DecimalField(max_digits=100, decimal_places=3)
    yIntercept = models.DecimalField(
        max_digits=100, decimal_places=3, default=0.000)
    dateTime = models.DateTimeField(auto_now_add=False)

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
