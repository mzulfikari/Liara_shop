from django.shortcuts import render
from django.views.generic import DetailView
from Products.models import Products


class ProductDetails(DetailView):
    template_name = "product\single-product.html"
    model = Products

