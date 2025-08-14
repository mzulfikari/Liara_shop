from django.contrib import messages
from urllib import request
from django.shortcuts import render
from django.views.generic import DetailView,ListView
from Products.models import Products,Comment,Color
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404,render,redirect


class ProductDetails(DetailView):
    template_name = "Product/single-product.html"
    model = Products
    context_object_name = 'products'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'  
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['colors'] = product.color.all()  # نه product.colors و نه product.Color
        return context
    
    def post(self, request, pk):
        
     if request.user.is_authenticated:
        self.object = self.get_object()
        parent_id = request.POST.get('parent_id')
        body = request.POST.get('body')
        
        if body:
         Comment.objects.create(
        body=body,
        products=self.object,
        user=request.user,
        parent_id=parent_id
    )
        else:
          messages.error(request, "متن نظر نمی‌تواند خالی باشد.")
        return redirect(request.path)
    


class Product_View(ListView):
    model = Products
    template_name = "Product/index.html"
    context_object_name = 'Products'


class Product_list(ListView):
    model = Products
    template_name = "Product/list_view.html"
    context_object_name = 'Products'
    

def search(request):
    Search = request.GET.get('search')
    Products_lists = Products.objects.filter(title__icontains = Search)
    page_number = request.GET.get('page')
    print(Products_lists)
    print(Search )
    paginator = Paginator(Products, 10)
    object_list = paginator.get_page(page_number)
    return render(request, "includes/head.html", {"Products": object_list})



