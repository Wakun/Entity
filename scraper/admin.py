from django.contrib import admin

from .models import Product, Category, File

class ProductAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Nazwy i numer', {'fields': ['art_name', 'auchan_name', 'plu_num']}),
        ('Kategoria', {'fields': ['category']}),
        ('Ceny', {'fields': ['auchan_price', 'rtveuro_price', 'mediamarkt_price', 'mediaexpert_price']}),
        ('Linki', {'fields': ['rtveuro_url', 'mediamarkt_url', 'mediaexpert_url']}),
    ]

    list_display = ('plu_num', 'art_name', 'auchan_name', 'category', 'auchan_price', 'rtveuro_price',
                    'mediamarkt_price', 'mediaexpert_price')

    search_fields = ['plu_num']

class CategoryAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Nazwa kategorii', {'fields': ['category_name']})
    ]

    list_display = ('id', 'category_name')

    search_fields = ['category_name']

class FileAdmin(admin.ModelAdmin):

    list_display = ('file', 'uploaded_at')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(File, FileAdmin)