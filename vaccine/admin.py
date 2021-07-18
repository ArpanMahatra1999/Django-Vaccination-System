from django.contrib import admin

from vaccine.models import Vaccine, Dose, Schedule

# Register your models here.
admin.site.register([Vaccine, Dose, Schedule])
