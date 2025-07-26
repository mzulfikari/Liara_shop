from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import ListView,View,TemplateView
from django.urls import reverse
from account.models import User
from .forms import AddressAdd,Change_Profile
from .models import *


def UserProfile(request):
    user = request.user
    context = {
        'profile': user,
    }
    return render(request, 'profile/profile.html', context)


def Change_profile(request):
    user = request.user
    form = Change_Profile(instance=user)
    if request.method == 'POST':
        form = Change_Profile(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Profile:Address')
    return render(request , "profile/profile-change-password.html",{"form": form})


class AddressView(ListView):
    template_name = 'profile/profile-address.html'
    model = Address
    context_object_name = 'Address'
    
    def post(self, request):
        user = request.user

        if 'delete_address' in request.POST:
            address_id = request.POST.get('delete_address')
            address = get_object_or_404(Address, pk=address_id, user=user)
            address.delete()

        elif 'set_default' in request.POST:
            address_id = request.POST.get('set_default')
            address = get_object_or_404(Address, pk=address_id, user=user)
            
            Address.objects.filter(user=user, is_default=True).update(is_default=False)

            address.is_default = True
            address.save()
           
        return redirect('Profile:Address')
        

class Address_Add(View):
    
    def post(self,request):
        user = request.user
        if Address.objects.filter(user=user).count() >= 3:
            messages.error(request, 'شما فقط می‌توانید ۳ آدرس ثبت کنید.')
            return redirect('Profile:Address')
        
        form = AddressAdd(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            
            address.save()
            
            return redirect('Profile:Address') 
        else:      
            return render (request,'profile/profile-address-edit.html',{'form':form})
        
    def get (self,request):
        form = AddressAdd()
        return render (request,'profile/profile-address-edit.html',{'form':form})
            

