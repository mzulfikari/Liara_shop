from django.urls import path
from . import views

app_name = 'Profile'

urlpatterns = [
    path('profile_view',views.UserProfile,name='Profile_View'),
    path('profile/address_add',views.Address_Add.as_view(),name='Address_add'),
    
    
]
    
