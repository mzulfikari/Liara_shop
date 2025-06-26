from django.db import models
from django.utils.html import format_html
from account.models import User

class Category(models.Model):
    title = models.CharField(
        max_length=50,verbose_name="عنوان"
        )
    created = models.DateTimeField(
        auto_now_add=True,verbose_name="تاریخ ایجاد"
        )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "دسته بندی ها"


class Size(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural ="سایز"



class Color(models.Model):
    title = models.CharField(
        max_length=30,verbose_name="عنوان رنگ",blank=True,null=True
        )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "رنگ بندی "


class Brand(models.Model):
    title = models.CharField(
        max_length=60,verbose_name="برند",blank=True,null=True
        )

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "برند ها "


class Products(models.Model):
    title = models.CharField(
        max_length=60,verbose_name="عنوان"
        )
    image = models.ImageField(
        upload_to="product/image",blank=True,null=True,verbose_name="بارگذاری تصویر"
        )
    price = models.SmallIntegerField(
        verbose_name="قیمت"
        )

    value = models.SmallIntegerField(
        verbose_name="مقدار"
        )
    Category = models.ManyToManyField(
        Category, related_name="Category",verbose_name="دسته بندی ها"
        )
    size = models.ManyToManyField(
        Size,blank=True,related_name='product'
        )
    color = models.ManyToManyField(
        Color,related_name='product',verbose_name="رنگ بندی ها"
        )

    def __str__(self):
        return self.title

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="78 px" height="50" />')
        return format_html('<h3 style="color: red">تصویر ندارد</h3>')
    show_image.short_description = " تصاویر"

    class Meta:
        verbose_name_plural = "محصولات"



class Comment(models.Model):
    products = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="comments",verbose_name="محصول"
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments",verbose_name="کاربر"
        )
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="replies", null=True,blank=True,verbose_name="پاسخ ها "
        )
    body = models.TextField(
        verbose_name="نظر"
        )
    created_at =models.DateTimeField(
        auto_now_add=True,verbose_name="تاریخ ایجاد"
        )

    def __str__(self):
        return self.Post.title
    class Meta:
        verbose_name_plural = 'کامنت ها'

