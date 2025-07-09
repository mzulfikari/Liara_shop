from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView,TemplateView
from Products.models import Products


class ProductDetails(TemplateView):
    template_name = "Product/single-product.html"
    model = Products


class ProductViews(TemplateView):
    template_name = "Product/index.html"
