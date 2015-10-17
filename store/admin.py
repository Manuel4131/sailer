from django.contrib import admin
from .models import Store, client

# Register your models here.

# admin.site.register(Store)
# @admin.register(Store)
# class StoreAdmin(admin.ModelAdmin):
# 	list_display = ('name','address') 


@admin.register(client)
class clientAdmin(admin.ModelAdmin):
	list_display=('firstName','lastName')