from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from Products.models import Products

class CartDetail(View):
    def get (self,request):
        return render(request,'cart/cart.html',{})


class CartAddView(View):
    def post(slef,request,pk):
        product = get_object_or_404(Products,id=pk)
        color = request.POST.get('color')
        size = request.POST.get('size')
        value = request.POST.get('value')

        return redirect('cart/cart.html')