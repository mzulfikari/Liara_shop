from django.urls import path
from .import views

# نام اپ کاربران
app_name="Product"

urlpatterns = [
   path('product/<int:pk>',views.ProductDetails.as_view(), name='Product_details'),
   path('',views.Product_View.as_view(), name='Product_view'),



]