from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from account.models import User
from .forms import AddressAdd



def UserProfile(request):
    user = request.user
    context = {
        'profile': user,
    }
    return render(request, 'profile/profile.html', context)


def Address_Add(request):
    if request.method == 'GET':
        Form = AddressAdd(data=request.GET)
        if Form.is_valid():
            title = Form.changed_data['title']
            receiver_name = Form.cleaned_data['receiver_name']
            phone_number = Form.cleaned_data['phone_number']
            city = Form.cleaned_data['city']
            province = Form.cleaned_data['province']
            postal_code = Form.cleaned_data['postal_code']
            full_address = Form.cleaned_data['full_address']
             
            AddressAdd.objects.create(
                title=title,receiver_name=receiver_name,phone_number=phone_number,city=city,
                province=province,postal_code=postal_code,full_address=full_address
                )
            return redirect('/')
    else:
        Form = AddressAdd
    return render(request,"profile/profile-address-edit.html",{"form": Form})
