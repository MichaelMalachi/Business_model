from django.shortcuts import render
from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'

import requests
from django.shortcuts import render

def product_list(request):
    response = requests.get('http://127.0.0.1:8000/api/products/')
    products = response.json()
    return render(request, 'product_list.html', {'products': products})
