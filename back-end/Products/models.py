from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from account.models import User
from  django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(
        max_length=50,verbose_name="عنوان"
        )
    created = models.DateTimeField(
        auto_now_add=True,verbose_name="تاریخ ایجاد"
        )

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
        max_length=80,verbose_name="عنوان"
        )
    hover_title = models.CharField(
        max_length=60,verbose_name="عنوان معرفی",blank=True,null=True
        )
    image = models.ImageField(
        upload_to="product/image",blank=True,null=True,verbose_name="بارگذاری تصویر"
        )
    price = models.SmallIntegerField(
        verbose_name="قیمت"
        )
    caption = models.TextField(
        verbose_name='درباره محصول'
        )
    value = models.SmallIntegerField(
        verbose_name="مقدار"
        )
    category = models.ForeignKey(
    Category,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="دسته بندی"
        )
    size = models.ManyToManyField(
        Size,blank=True,related_name='product'
        )
    color = models.ManyToManyField(
        Color,related_name='product',verbose_name="رنگ بندی ها"
        )
    slug = models.SlugField(
        blank=True , unique=False ,verbose_name="به صورت خودکار از عنوان محصول استفاده میشود",null=True
        )
    inventory = models.BooleanField(
        default=True,verbose_name="موجودیت"
        )
    # brand = models.ForeignKey(
    #     Brand,verbose_name='برند'
    # )

    def __str__(self):
        return self.title

    def show_image(self):
        """To display images in the management panel"""

        if self.image:
            return format_html(f'<img src="{self.image.url}" width="78 px" height="50" />')
        return format_html('<h3 style="color: red">تصویر ندارد</h3>')
    show_image.short_description = " تصاویر"


    def save(self,force_insert=False,force_update=False,using=None,
             update_fields=None):
        self.slug = slugify(self.title)
        super(Products, self).save()

    def get_absolute_url(self):
        return reverse('blog:Post_details', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = "محصولات"


class Comment(models.Model):
    """Implementation of the questions section,
    which features questions and answers after login"""

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
        return self.products.title
    class Meta:
        verbose_name_plural = 'کامنت ها'


class Like(models.Model):
    """
    Implementation of users'
    like section is a feature that is considered to
    be viewed after login
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="likes"
        )
    products = models.ForeignKey(
        Products, on_delete=models.CASCADE, related_name="likes"
        )
    created_at = models.DateTimeField(
        auto_now_add=True
        )

    def __str__(self):
        return f"{self.user.username} - {self.products.title}"

    class Meta:
        verbose_name = 'پسند'
        verbose_name_plural = 'پسند ها'
        ordering = ( '-created_at',)