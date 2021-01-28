from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.recipe)
admin.site.register(models.rekomend)
admin.site.register(models.favorit)