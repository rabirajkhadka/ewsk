from django.db import models
from threading import Thread, current_thread


class Dataset(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(auto_now_add=True)
    water_level = models.DecimalField(max_digits=20, decimal_places=12)
    delay_time = models.IntegerField()


# @property
# def get_average(self):
   # avg = self.water_level * self.delay_time
    # return avg


class River(models.Model):
    rid = models.AutoField(primary_key=True)
    river_name = models.CharField(max_length=200, null=True)
    river_location = models.CharField(max_length=200, null=True)
    river_trend = models.CharField(max_length=200, null=True)


class WarningMessage(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(auto_now_add=True)
    warning_id = models.IntegerField
    warninig_value = models.FloatField
    river_trend = models.CharField(max_length=200, null=True)


class WarningLevel(models.Model):
    warning_id = models.AutoField(primary_key=True)
    river = models.ForeignKey(
        River, on_delete=models.CASCADE, blank=True, null=True)
    value = models.FloatField()


class Station(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=200, null=True)
    station_location = models.CharField(max_length=200, null=True)
    river = models.ForeignKey(
        River, on_delete=models.CASCADE, blank=True, null=True)


class DangerLevel(models.Model):
    danger_id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=200, null=True)
    rid = models.ForeignKey(
        River, on_delete=models.CASCADE, blank=True, null=True)


class WaterLevelStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=200, null=True)


class WaterLevel(models.Model):
    level_id = models.AutoField(primary_key=True)
    water_level = models.FloatField()
    date_time = models.DateTimeField()
    rid = models.ForeignKey(
        River, on_delete=models.CASCADE, blank=True, null=True)
    status_id = models.ForeignKey(
        WaterLevelStatus, on_delete=models.CASCADE, blank=True, null=True)
    warning_id = models.ForeignKey(
        WarningLevel, on_delete=models.CASCADE, blank=True, null=True)
    danger_id = models.ForeignKey(
        DangerLevel, on_delete=models.CASCADE, blank=True, null=True)


class WarningDataset(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.FloatField()
    image = models.ImageField()
