from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import Otp, User
from account.forms import UserChangeForm, UserCreationForm

admin.site.site_header = 'پنل مدیریت فروشگاه'

class UserAdmin(BaseUserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm


    list_display = ["phone","first_name","last_name", "is_admin","email"]
    list_filter = ["is_admin"]
    fieldsets = [
        ("مشخصات  کاربر لاگین ", {"fields": ["phone", "password","first_name","last_name","image","email"]}),
        ("وضعیت کاربر", {"fields": ["is_admin","is_active"]}),
        ("آخرین ورود", {"fields": ["last_login"]}),
        (" احراز هویت", {"fields": ["verification_time","Authentication"]}),

    ]

    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "phone", "password1", "password2","first_name","last_name",
                    "Authentication","verification_time","email","image","last_login","national_code",],
            },
        ),
    ]
    search_fields = ["phone"]
    ordering = ["phone"]
    filter_horizontal = []

@admin.register(Otp)
class OTPAdmin(admin.ModelAdmin):
    list_display = ("phone", "code",)

admin.site.register(User, UserAdmin)

admin.site.unregister(Group)
