from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
import django_tables2 as tables

from .models import Product

def index(request):
    return render(request, 'scraper/index.html')

class ProductsListTable(tables.Table):
    plu_num = tables.Column()
    art_name = tables.Column()
    rtveuro_price = tables.Column()
    mediamarkt_price = tables.Column()
    mediaexpert_price = tables.Column()

@login_required(login_url='/login')
def products_list(request):

    products = Product.objects.defer('art_name', 'plu_num', 'mediaexpert_price', 'mediamarkt_price', 'rtveuro_price')

    table = ProductsListTable(products)
    tables.RequestConfig(request).configure(table)

    return render(request, 'scraper/products_list.html', {'products_list': table})

def add_product(request):
    pass