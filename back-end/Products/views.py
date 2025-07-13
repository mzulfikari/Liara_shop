from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView,TemplateView,ListView
from Products.models import Products , Category
from django.core.paginator import Paginator
from collections import defaultdict
from django.db.models import Prefetch


class ProductDetails(DetailView):
    template_name = "Product/single-product.html"
    model = Products

class Product_View(ListView):
    model = Products
    template_name = "Product/index.html"
    context_object_name = 'Products'


def search(request):
    Search = request.GET.get('search')
    Products_lists = Products.objects.filter(title__icontains = Search)
    page_number = request.GET.get('page')
    print(Products_lists)
    print(Search )
    paginator = Paginator(Products, 10)
    object_list = paginator.get_page(page_number)
    return render(request, "blog/Post_list.html", {"Products": object_list})
