from django.contrib import admin
from . import models
from Products.models import Category,Size,Color,Brand,Comment
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin

class CommentInline(admin.StackedInline):
    model = Comment

class InformationAdmin(admin.StackedInline):
    model = models.Information


@admin.register(models.Products)
class ProductAdmin(admin.ModelAdmin):
    inlines = (InformationAdmin,CommentInline,
               )
    list_display = (
        "title",
        "price",
        "views",
        "stock_count",
        "created",
        "show_image",)

    list_editable=(
        "price",
        )
    search_fields=(
        "title",
        )
    list_filter = (
            "category",
            "inventory",
            "created",
            )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",
                    "created",
                    "show_image",)
    list_filter = ("created",)
    search_fields = ("title",)

admin.site.register(Size)
list_display = (
        "title",
        )
admin.site.register(Color)
list_display = (
        "title",
        )
admin.site.register(Brand)
list_display = (
        "title",
        )

@admin.register(models.Comment)
class CommentAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['products', 'user', 'body', 'status', 'get_created_at_jalali']
    list_editable = ['status']
    actions = ['approve_comments']

    def short_product_title(self, obj):
        if len(obj.product.title) > 10:
            return obj.product.title[:10] + '...'
        return obj.product
    short_product_title.short_description = 'محصول مربوطه'

    def short_body(self, obj):
        if len(obj.body) > 20:
            return obj.body[:20] + '...'
        return obj.body
    short_body.short_description = 'متن دیدگاه'

    @admin.display(description='تاریخ ایجاد', ordering='created_at')
    def get_created_at_jalali(self, obj):
        return datetime2jalali(obj.created_at).strftime('%a, %d %b %Y')
    
    @admin.action(description='تأیید کامنت‌های انتخاب‌شده')
    def approve_comments(self, request, queryset):
        queryset.update(active=True)