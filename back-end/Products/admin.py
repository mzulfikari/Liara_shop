from django.contrib import admin
from . import models
from Products.models import Category,Size,Color,Brand,Comment

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
        "value",
        "show_image",)

    list_editable=(
        "price",
        "value",
        )
    search_fields=(
        "title",
        )
    list_filter = (
            "category",
            "price",
            'inventory',
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

admin.site.register(models.Comment)
list_display = (
        "user",
        "products",
        )