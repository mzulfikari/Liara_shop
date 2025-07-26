from django import forms
from .models import Address
from django.forms.widgets import TextInput
from django.core.exceptions import ValidationError
from django.contrib import messages
from account.models import User

class TelInput(TextInput):
    input_type = 'tel'

class AddressAdd(forms.ModelForm):
    user = forms.IntegerField(required=False)
    class Meta:
     model = Address
     fields = ('title','receiver_name','phone_number','city','province','postal_code','full_address','is_default','email',)
   
     widgets = {
            'title': forms.TextInput(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            "placeholder":
            "محل کار , منزل..."
            }),
            'receiver_name': forms.TextInput(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            "placeholder":
            " نام و نام خانوادگی تحویل گیرنده"
            }),
            'phone_number': forms.NumberInput(
            attrs={
            'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            "placeholder":
            "شماره همراه تحویل گیرنده"
            }),
            'city': forms.TextInput(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            "placeholder":
            "شهر"
            }),
            'province': forms.TextInput(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            "placeholder":
            "شهرستان"
            }),
            'postal_code': forms.NumberInput(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            "placeholder":
            "کدپستی"
            }),
            'email': forms.EmailInput(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            "placeholder":
            "ایمیل را وارد کنید (الزامی نیست)"}
            ),
            'full_address': forms.Textarea(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            "placeholder":
            "آدرس کامل"}
            ),
            'is_default': forms.CheckboxInput(
            attrs={'class':
            "form-checkbox h-5 w-5 text-blue-600 focus:ring-blue-500 cursor-pointer mr-1",
            })}


    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise ValidationError("عنوان آدرس باید حداقل 3 کاراکتر باشد.")
        if len(title) > 30:
            raise ValidationError("عنوان آدرس باید حداکثر 30 کاراکتر باشد.")
        return title

    def clean_full_address(self):
        full_address = self.cleaned_data.get('full_address')
        if len(full_address) < 10:
            raise ValidationError("آدرس باید حداقل 10 کاراکتر باشد.")
        if len(full_address) > 300:
            raise ValidationError("آدرس باید حداکثر 300 کاراکتر باشد.")
        return full_address

    def clean_city(self):
        city = self.cleaned_data.get('city')
        if len(city) < 2:
            raise ValidationError("استان باید حداقل 2 کاراکتر باشد.")
        if len(city) > 50:
            raise ValidationError("استان باید حداکثر 50 کاراکتر باشد.")
        return city

    def clean_province(self):
        province = self.cleaned_data.get('province')
        if len(province) < 2:
            raise ValidationError("شهرستان باید حداقل 2 کاراکتر باشد.")
        if len(province) > 50:
            raise ValidationError("شهرستان باید حداکثر 50 کاراکتر باشد.")
        return province

    def clean_postal_code(self):
        postal_code = self.cleaned_data.get('postal_code')
        if len(postal_code) != 10:
            raise ValidationError("کد پستی باید 10 رقم باشد.")
        if not postal_code.isdigit():
            raise ValidationError("کد پستی باید فقط شامل اعداد باشد.")
        return postal_code

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('09'):
            raise ValidationError("شماره تلفن باید با 09 شروع شود.")
        if len(phone_number) != 11:
            raise ValidationError("شماره تلفن باید 11 رقم باشد.")
        return phone_number

    def clean_receiver_name(self):
        receiver_name = self.cleaned_data.get('receiver_name')
        if len(receiver_name.split()) < 2:
            raise ValidationError("لطفا نام و نام خانوادگی تحویل گیرنده را وارد کنید.")
        return receiver_name
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is None:
            email = ''
        if email:
            if not email.endswith('@gmail.com'):
                raise ValidationError("لطفاً یک ایمیل معتبر با دامنه @gmail.com وارد کنید.")
            if len(email) < 15:
                raise ValidationError("ایمیل باید حداقل 15 کاراکتر باشد.")
            if len(email) > 100:
                raise ValidationError("ایمیل باید حداکثر 100 کاراکتر باشد.")
        return email

    
class Change_Profile(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone','first_name','last_name','email','national_code','card_number',)
        
        widgets = {
            'first_name': forms.TextInput(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            
            }),
             'last_name': forms.TextInput(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            
            }),
             'phone': forms.TextInput(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            
            }),
             'email': forms.TextInput(
            attrs={'class':
            "text-sm block w-full appearance-none rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            
            }),
             'national_code': forms.TextInput(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            
            }),
             'card_number': forms.TextInput(
            attrs={'class':
            "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
            
            }),
        }
  