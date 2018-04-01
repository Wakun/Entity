from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('art_name', 'plu_num', 'category', 'auchan_price', 'rtveuro_url', 'mediamarkt_url', 'mediaexpert_url')