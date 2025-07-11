from Products.models import Category, Products


def Categories(request):
    Categories = Category.objects.filter(views=True)
    return {'Categories': Categories}

def recent_Products(request):
    recent_Products= Products.objects.all().order_by('-created')[:8]
    return {'recent_Products':recent_Products}
