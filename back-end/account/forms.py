from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from account.models import User , Otp
from django.core import validators

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["phone", "last_name"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("گذرواژه ها مطابقت ندارند")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = User
        fields = ["phone", "password", "first_name","last_name", "is_active", "is_admin"]

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'w-full drop-shadow-lg outline-none rounded-2xl py-2 text-center',
            "placeholder":"شماره نام کاربری را وارد کنید"
            }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-full drop-shadow-lg outline-none rounded-2xl py-2 text-center'}))

    def clean_username(self):
       username = self.cleaned_data.get('username')
       if len(username) > 100:
            raise ValidationError('اطلاعات وارد شده صحیح نمی باشد',code='invalid phone' )
       return username

class RegisterForm(forms.ModelForm):
    first_name = forms.CharField (
    widget=forms.TextInput(attrs={'class': 'w-full drop-shadow-lg outline-none rounded-2xl py-2 text-center'}),
    max_length=11)
    
    last_name = forms.CharField (
    widget=forms.TextInput(attrs={'class': 'w-full drop-shadow-lg outline-none rounded-2xl py-2 text-center'})
    ,min_length=11, max_length=11)
    
    phone = forms.CharField (
    widget=forms.TextInput(attrs={'class': 'w-full drop-shadow-lg outline-none rounded-2xl py-2 text-center'})
    ,min_length=11, max_length=11)


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if not phone.isdigit():
            raise ValidationError("شماره تلفن فقط باید شامل ارقام باشد.")

        if not phone.startswith("09"):
            raise ValidationError("شماره تلفن باید با 09 شروع شود.")

        return phone

    class Meta:
        model = User
        fields = ['phone',]


class CheckOtpform(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full drop-shadow-lg outline-none rounded-2xl py-2 text-center'})
     ,max_length=4)

    class Meta:
        model = Otp
        fields = ['code']


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input_second input_all', 'placeholder': 'رمز عبور فعلی'}
        )
    )
    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'input_second input_all', 'placeholder': 'رمز عبور جدید'}
        )
    )
    confirm_new_password = forms.CharField(
         widget=forms.PasswordInput(attrs={'class': 'input_second input_all', 'placeholder': 'تکرار رمز عبور جدید'}
        )
    )

    def clean_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        if len(new_password) < 8:
            raise ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد.")
        if len(new_password) > 20:
            raise ValidationError("رمز عبور نباید بیشتر از 20 کاراکتر باشد.")
        return new_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if new_password and confirm_new_password and new_password != confirm_new_password:
            raise ValidationError("رمز عبور جدید و تکرار آن مطابقت ندارند.")
        return cleaned_data