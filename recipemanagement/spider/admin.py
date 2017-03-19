from django.contrib import admin

# Register your models here.
from .models import Spider
class SpiderAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            )
admin.site.register(Spider, SpiderAdmin)
