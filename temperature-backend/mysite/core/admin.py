from django.contrib import admin
from .models import Temperature,Record,Location,Sensor
# Register your models here.

admin.site.register(Temperature)
admin.site.register(Record)
admin.site.register(Location)
admin.site.register(Sensor)