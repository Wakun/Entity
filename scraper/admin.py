from django.contrib import admin

from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Nazwy i numer', {'fields': ['art_name', 'auchan_name', 'plu_num']}),
        ('Kategoria', {'fields': ['category']}),
        ('Ceny', {'fields': ['auchan_price', 'rtveuro_price', 'mediamarkt_price', 'mediaexpert_price']}),
        ('Linki', {'fields': ['rtveuro_url', 'mediamarkt_url', 'mediaexpert_url']}),
    ]

    list_display = ('plu_num', 'art_name', 'auchan_name', 'category', 'auchan_price', 'rtveuro_price',
                    'mediamarkt_price', 'mediaexpert_price')

class CategoryAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Nazwa kategorii', {'fields': ['category_name']})
    ]

    list_display = ('id', 'category_name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)