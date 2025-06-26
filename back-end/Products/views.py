from django.shortcuts import render
from django.views.generic import DetailView,TemplateView
from Products.models import Products


class ProductDetails(DetailView):
    template_name = "Product\single-product.html"
    model = Products

