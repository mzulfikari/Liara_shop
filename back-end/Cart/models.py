from django.db import models
from account.models import User
from django.utils.translation import gettext as _
from.module import Cart
from Products.models import Products

# class Cart(models.Model):
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='cart'
#         )
#     send_price = models.PositiveIntegerField(
#         _('هزینه ی ارسال'), default=0, help_text='به تومان'
#         )
#     created = models.DateField(
#         _('تاریخ ایجاد'), auto_now_add=True
#         )
#     updated = models.DateField(
#         _('تاریخ آپدیت'), auto_now=True
#         )

#     class Meta:
#         verbose_name = "سبد خرید"
#         verbose_name_plural = "سبد خرید"


# class CartItem(models.Model):
#     cart = models.ForeignKey(
#         Cart, on_delete=models.CASCADE, related_name="cart_items", verbose_name='سبد خرید'
#         )
#     product = models.ForeignKey(
#         Products, on_delete=models.CASCADE, null=True, blank=True, verbose_name='محصول'
#         )
#     quantity = models.DecimalField(
#         _('تعداد'), default=1.0, max_digits=12, decimal_places=7
#         )

#     created = models.DateField(
#         _('تاریخ ایجاد'), auto_now_add=True
#         )
#     updated = models.DateField(
#         _('تاریخ آپدیت'), auto_now=True
#         )

#     class Meta:
#         verbose_name = "آیتم سبد خرید"
#         verbose_name_plural = "آیتم سبد خرید"
