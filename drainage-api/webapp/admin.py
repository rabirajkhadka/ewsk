from django.contrib import admin
from .models import Station, WarningMessage, WarningMessageData, DrainageTrend, Average, DataSet

admin.site.register(Station)
admin.site.register(WarningMessage)
admin.site.register(WarningMessageData)
admin.site.register(DrainageTrend)
admin.site.register(Average)
admin.site.register(DataSet)
