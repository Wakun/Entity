from django.conf.urls import url

from . import views

app_name = 'scraper'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^productslist/$', views.products_list, name='Lista produktów'),
    url(r'^productslist/(?P<pk>\d+)/$', views.product_view, name='Edycja produktu'),
    url(r'^addproduct/$', views.add_product, name='Dodaj produkt'),
    url(r'^scrapprices/$', views.scrap_prices, name='Pobierz ceny'),
    url(r'^uploadauchanprices/$', views.upload_auchan_prices, name='Ceny dyskont'),


]