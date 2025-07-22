from django import forms
from .models import Address


class AddressAdd(forms.ModelForm):
    
  class Meta:
    model = Address
    fields = ('title','receiver_name','phone_number','city','province','postal_code','full_address')
    widgets = {
        'title': forms.TextInput(
                attrs={'class':"text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
                "placeholder":"محل کار , منزل ... "}
                ),
            'receiver_name': forms.TextInput(
                attrs={'class':"text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
                "placeholder":" لطفا نام و نام خانوداگی تحویل گیرنده را وارد کنید"}
                ),
            'phone_number': forms.TextInput(
                attrs={'class': "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
                       "placeholder":"شماره تلفن تحویل گیرنده را وارد کنید"}
                ),
            'city': forms.TextInput(
                attrs={'class': "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
                       "placeholder":"شهر مورد نظر را وارد کنید"}
                ),
            'province': forms.TextInput(
                attrs={'class': "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
                       "placeholder":"شهرستان مورد نظر را وارد کنید"}
                ),
            'postal_code': forms.TextInput(
                attrs={'class': "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
                       "placeholder":"کد پستی را وارد کنید"}
                ),
            'full_address': forms.TextInput(
                attrs={'class': "text-sm block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 font-normal text-gray-700 outline-none focus:border-red-300",
                       "placeholder":"آدرس کامل خود را وارد کنید"}
                )
        }
