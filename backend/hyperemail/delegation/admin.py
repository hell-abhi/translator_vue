from django.contrib import admin

# Register your models here.

from .models import User, Helper

class UserDetails(admin.ModelAdmin):
    list_display = ("first_name","last_name","email_id")

class HelperDetails(admin.ModelAdmin):
    list_display = ("user", "connected_email", "connected_folder")

admin.site.register(User, UserDetails)
admin.site.register(Helper, HelperDetails)