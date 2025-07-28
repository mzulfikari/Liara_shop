from django.contrib.auth import authenticate , login, logout
from django.contrib.auth import update_session_auth_hash
from pyexpat.errors import messages
from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import ListView,View
from django.urls import reverse
from account.models import User
from .forms import AddressAdd, Change_Password,Change_Profile
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
    return render(request , "profile/profile-change.html",{"form": form})


class ChangePassword(View):
    def get(self, request):
        form = Change_Password()
        context = {
            'profile': request.user,  
            'form': form,
        }
        return render(request, 'profile/change-password.html', context)


# class ChangePassword(View):
    
#  def post(self, request):
#      form = Change_Password(request.POST)
#      profile = get_object_or_404(User,user=request.user)

#      if request.method == 'POST':
#         form = Change_Password(request.POST)
#         if form.is_valid():
#             old_password = form.cleaned_data['old_password']
#             new_password = form.cleaned_data['new_password']

#             if request.user.check_password(old_password):
#                 request.user.set_password(new_password)
#                 request.user.save()
#                 update_session_auth_hash(request, request.user)
#                 logout(request)
#                 messages.success(request, 'رمز عبور شما با موفقیت تغییر یافت. لطفاً با رمز عبور جدید وارد شوید.')
#                 return redirect('account:Login-user')
#             else:
#                 form.add_error('old_password', 'رمز عبور فعلی نادرست است.')
#      else:
#         form = Change_Password()

#      context = {
#         'profile': profile,
#         'form': form,
#     }
#      return render(request, 'profile/change-password.html', context)


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
     
     
  