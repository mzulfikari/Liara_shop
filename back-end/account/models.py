from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
from account.managment.managment import UserManager
from django.utils.translation import gettext as _

#پروفایل کاربر
class User(AbstractBaseUser):
    phone = models.CharField(
        verbose_name="شماره تلفن",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        max_length=50,verbose_name='نام'
        )
    last_name = models.CharField(
        max_length=50, verbose_name='نام خانوادگی'
        )
    verification_time = models.DateField(
        null=True, blank=True
        )
    is_active = models.BooleanField(
        default=True
        )
    is_admin = models.BooleanField(
        default=False
        )
    email = models.EmailField(
        verbose_name= 'ایمیل'
        )
    image = models.ImageField(
        upload_to="images/", null=True, blank=True,verbose_name='پروفایل'
        )
    Authentication = models.BooleanField(
        default=False,verbose_name='وضعیت احراز هویت'
        )
    password = models.CharField(
        max_length=300
        )
    last_login = models.DateTimeField(
        _("last login"), blank=True, null=True
        )
    objects = UserManager()

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):

        return self.is_admin

    class  Meta:
        verbose_name_plural = 'کاربران'


#ریجستر و احراز هویت شماره تلفن
class Otp(models.Model):
    token = models.CharField(max_length=200, null=True,verbose_name='توکن')
    phone = models.CharField(max_length=11,verbose_name='شماره تلفن')
    code = models.SmallIntegerField(verbose_name='کد یکبار مصرف')
    expiration_date = models.DateTimeField(auto_now_add=True,verbose_name='مدت زمان اعتبار کد')

    def __str__(self):
        return self.phone
    class  Meta:
       verbose_name_plural ='یکبار مصرف '
