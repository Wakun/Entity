from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import django_tables2 as tables
from django_tables2.utils import A

from .models import Product
from .forms import ProductForm

def index(request):
    return render(request, 'scraper/index.html')

class ProductsListTable(tables.Table):
    plu_num = tables.Column()
    art_name = tables.Column()
    rtveuro_price = tables.Column()
    mediamarkt_price = tables.Column()
    mediaexpert_price = tables.Column()
    edit_link = tables.LinkColumn('scraper:Edycja produktu', args=[A('pk')], text='Edytuj', empty_values=(), verbose_name='Edycja')


@login_required(login_url='/login')
def products_list(request):

    products = Product.objects.all()

    table = ProductsListTable(products)
    tables.RequestConfig(request).configure(table)

    return render(request, 'scraper/products_list.html', {'products_list': table})

@login_required(login_url='/login')
def add_product(request):

    if request.method == 'POST':

        form = ProductForm(request.POST)

        if form.is_valid():
            product = form.save()
            product.save()
            return redirect('scraper:Dodaj produkt')

    else:
        form =  ProductForm()

    return render(request, 'scraper/add_product.html', {'form': form})

def product_view(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':

        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            product = form.save()
            product.save()
            return redirect('scraper:Lista produktów')

    else:

        form = ProductForm(instance=product)

    return render(request, 'scraper/product_view.html', {'form': form})