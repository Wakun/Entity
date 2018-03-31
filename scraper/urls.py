from django.conf.urls import url

from . import views

app_name = 'scraper'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^productslist/$', views.products_list, name='Lista produktów'),

]