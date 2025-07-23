from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import TemplateView,ListView,View
from django.contrib.auth.decorators import login_required
from account.models import User
from .forms import AddressAdd
from .models import *

def UserProfile(request):
    user = request.user
    context = {
        'profile': user,
    }
    return render(request, 'profile/profile.html', context)

 
class Details_Address(ListView):
    template_name = 'profile/profile-address.html'
    model = Address
    context_object_name = 'Address'

class Address_Add(View):
    
    def post(self,request):
        form = AddressAdd(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            
            return redirect('/') 
        else:      
            return render (request,'profile/profile-address-edit.html',{'form':form})
        
    def get (self,request):
        form = AddressAdd()
        return render (request,'profile/profile-address-edit.html',{'form':form})
            