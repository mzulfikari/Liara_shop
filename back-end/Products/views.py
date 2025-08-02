from urllib import request
from django.shortcuts import render
from django.views.generic import DetailView,ListView
from Products.models import Products,Comment
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404,render,redirect


class ProductDetails(DetailView):
    template_name = "Product/single-product.html"
    model = Products
    context_object_name = 'products'
    slug_url_kwarg = 'slug'
    slug_field = 'slug'  
    
    # def get(self,requst):
    #     comments = Products.product_comments.filter(status='published').order_by('-created_at')
        
    #     view_products = request.session.get('viewed_products', [])
    #     if Products.id not in view_products:
    #      Products.views += 1
    #      Products.save(update_fields=['views'])
    #     view_products.append(Products.id)
    #     request.session['viewed_products'] = view_products
        
    
    

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



