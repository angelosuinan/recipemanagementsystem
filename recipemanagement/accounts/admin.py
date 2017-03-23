from django.contrib import admin

# Register your models here.i

from . models import Account

class AccountAdmin(admin.ModelAdmin):
    list_display =(
            'f_name',
            'l_name',
            'active',
            )
admin.site.register(Account, AccountAdmin)
