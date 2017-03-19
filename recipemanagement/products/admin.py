from django.contrib import admin

from .models import Recipe, Product

class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    list_filter = (
        'created_time',
        'modified_time',
        'active',
    )
    search_fields = (
            'name',
    )
    readonly_fields = (
        'created_time',
        'modified_time',
    )
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'modified_time',
        'price'
    )
    list_filter = (
        'created_time',
        'modified_time',
        'active',
    )
    search_fields = (
            'name',
    )
    readonly_fields = (
        'created_time',
        'modified_time',
    )
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Product, ProductAdmin)

