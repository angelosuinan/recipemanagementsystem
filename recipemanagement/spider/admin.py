from django.contrib import admin

# Register your models here.
from .models import Spider
def run_spider(modeladmin, request, queryset):
    run_spider.short_description = "Run Spider"
def add_db(modeladmin, request, queryset):
    add_db.short_description = "Add CSV file to Database"
class SpiderAdmin(admin.ModelAdmin):
    list_display = [
            'name',
            'active'
            ]
    actions = [run_spider, add_db]
admin.site.register(Spider, SpiderAdmin)
