
from django.contrib import admin
from django.urls import path
from business_model.views import HomeView
from business_model.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('products/', product_list, name='product_list'),
]
