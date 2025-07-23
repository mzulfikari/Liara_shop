from django.contrib import admin
from . import models
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin

@admin.register(models.Address)
class Address(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'title', 'receiver_name', 'city','get_created_at_jalali']

    @admin.display(description='تاریخ ارسال', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b  %Y _ %H:%M')
    