from django.contrib import admin

# Register your models here.i

from . models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display =(
            'name',
            'f_name',
            'l_name',
            'active',
            'price',
            )
admin.site.register(Account, AccountAdmin)
