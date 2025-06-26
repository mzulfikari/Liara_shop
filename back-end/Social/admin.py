from django.contrib import admin
from . import models
from .models import Utm_info,Utm_access

@admin.register(models.Utm_info)
class Utm_info(admin.ModelAdmin):
    list_display = (
        "platform",
        "utm_source",
        "utm_medium",
        "utm_campaign",
        "created_at",
        )
    list_filter = (
        "utm_source",
        "platform",
        )
    readonly_fields = ['sharing_url', 'created_at']

@admin.register(models.Utm_access)
class Utm_Admin(admin.ModelAdmin):
    list_display = (
        "user_admin",
        "utm_info",
        "access_level",
        "granted_at",
        )
    list_editable = (
        "access_level",

        )

@admin.register(models.Log_Utm)
class Utm_Logs(admin.ModelAdmin):
    list_display = (
        "platform",
        "url",
        )
    list_filter = (
        "platform",
        "url"
        )

@admin.register(models.Platform)
class Utm_Admin(admin.ModelAdmin):
    list_display = (
        "title",
        )


