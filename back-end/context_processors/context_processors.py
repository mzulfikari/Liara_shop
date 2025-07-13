from Products.models import Category, Products
from django.db.models import Prefetch


def Categories(request):
    """To display categories that have products
     Get categories that have at least one product
     Sort products by creation date and limit the number of products to 8 products"""

    Categories = Category.objects.filter(
        products__isnull=False
    ).distinct()

    prefetch = Prefetch('products', queryset=Products.objects.order_by('-created'))
    Categories = Categories.prefetch_related(prefetch)
    return {
        'Categories': Categories
        }

# def recent_Products(request):

#     recent_Products= Products.objects.all().order_by('-created')[:8]
#     return {
#         'recent_Products':recent_Products
#         }
