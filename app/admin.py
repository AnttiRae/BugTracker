from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Bug)
admin.site.register(models.Comment)