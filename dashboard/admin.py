from django.contrib import admin


# Register your models here.
from .models import *

admin.site.register(Dataset)
admin.site.register(River)
admin.site.register(WarningLevel)
admin.site.register(WaterLevel)
admin.site.register(WaterLevelStatus)
admin.site.register(DangerLevel)
admin.site.register(Station)
admin.site.register(WarningMessage)
admin.site.register(WarningDataset)
