from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import format_html


STATUS = (
    ("draft", "پیش نویس شود"),
    ("published", "منتشر شود"),
)

class SiteSettings(models.Model):
    
    logo = models.ImageField( 
        upload_to='logo/image',null=True,blank=True,verbose_name='لوگو'
        )
    text_about_us = RichTextUploadingField(
        null=True, blank=True, verbose_name='متن درباره ما'
        )
    address = models.CharField(
        max_length=250, null=True, blank=True, verbose_name='آدرس'
        )
    phone1 = models.CharField(
        max_length=14, null=True, blank=True, verbose_name='شماره تلفن همراه'
        )
    phone2 = models.CharField(
        max_length=14, null=True, blank=True, verbose_name='شماره تلفن ثابت'
        )
    email1 = models.CharField(
        max_length=250, null=True, blank=True, verbose_name='ایمیل '
        )
    instagram_link = models.CharField(
        max_length=250, null=True, blank=True, default='https://instagram.com/username', verbose_name='لینک اینستاگرام'
        )
    telegram_link = models.CharField(
        max_length=250, null=True, blank=True, default='https://t.me/username', verbose_name='لینک تلگرام'
        )
    

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'


class Banner(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='عنوان بنر'
        )
    image = models.ImageField(
        upload_to='banners/', verbose_name='تصویر بنر'
        )
    status = models.CharField(
        choices=STATUS, max_length=10, default='published', verbose_name='وضعیت'
        )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد'
        )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='تاریخ به‌روزرسانی'
        )
    
    class Meta:
        verbose_name = 'بنر'
        verbose_name_plural = 'بنر ها'


    def banner_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="100px" height="50px">')
        return format_html(f'<h3 style="color: red">تصویر ندارد</h3>')

    def __str__(self):
        return self.title
    
    
    
class ContactUs(models.Model):
    first_name = models.CharField(
        max_length=100, verbose_name='نام'
        )
    last_name = models.CharField(
        max_length=100, verbose_name='نام خانوادگی'
        )
    phone = models.CharField(
        max_length=14, verbose_name='شماره تماس'
        )
    message = models.TextField(
        verbose_name='متن پیام'
        )
    date_send = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ارسال'
        )

    class Meta:
        ordering = ["-date_send"]
        verbose_name = "تماس با ما"
        verbose_name_plural = "تماس با ما"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'