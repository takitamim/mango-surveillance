from django.contrib import admin
from .models import Grower, Plant, SurveillanceRecord

admin.site.register(Grower)
admin.site.register(Plant)
admin.site.register(SurveillanceRecord)