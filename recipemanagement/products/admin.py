from django.contrib import admin

from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'img_url',
    )
    list_filter = (
        'created_time',
        'modified_time',
        'active',
    )
    search_fields = (
        'title',
        'description',
    )
    readonly_fields = (
        'created_time',
        'modified_time',
    )
admin.site.register(Recipe, RecipeAdmin)
