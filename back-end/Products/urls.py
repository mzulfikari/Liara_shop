from django.urls import path
from .import views

# نام اپ کاربران
app_name="Product"

urlpatterns = [
   path('product',views.ProductDetails.as_view(), name='product-details'),


]