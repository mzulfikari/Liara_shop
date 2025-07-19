from django.urls import path
from . import views

app_name = 'Cart'

urlpatterns = [
    path('cart',views.CartDetail.as_view(),name='Cart_datail'),
    path('cart/add/<int:pk>',views.CartAddView.as_view(),name='Cart_add')
]
