from django.contrib import admin
from . import models

admin.site.register(models.AudioContent)
admin.site.register(models.VideoContent)