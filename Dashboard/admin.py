from django.contrib import admin

# Register your models here.
from .models import Dataset, River, WarningLevel, WaterLevel, DangerLevel, Station, WaterLevelStatus

admin.site.register(Dataset)
admin.site.register(River)
admin.site.register(WarningLevel)
admin.site.register(WaterLevel)
admin.site.register(WaterLevelStatus)
admin.site.register(DangerLevel)
admin.site.register(Station)
