from Products.models import Category, Products
from django.db.models import Prefetch
from core.models import SiteSettings ,Banner

def Categories(request):
    """To display categories that have products
     Get categories that have at least one product
     Sort products by creation date and limit the number of products to 8 products"""

    Categories = Category.objects.filter(views=True,
        products__isnull=False
    ).distinct()

    prefetch = Prefetch('products', queryset=Products.objects.order_by('-created'))
    Categories = Categories.prefetch_related(prefetch)
    return {
        'Categories': Categories
        }


def site_settings(request):
    """Default site settings"""
    
    try:
        settings = SiteSettings.objects.first()
    except SiteSettings.DoesNotExist:
        settings = None
    return {'site_settings': settings}

def Banners(request):
    """Return only published banner objects ordered by creation date"""
    banner = Banner.objects.filter(status='published').order_by('-created_at')
    return {'Banners': banner}