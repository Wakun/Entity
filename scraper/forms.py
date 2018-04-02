from django import forms

from .models import Product, Category

class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.category_name

class ProductForm(forms.ModelForm):

    category = CustomModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ('art_name', 'auchan_name', 'plu_num', 'category', 'auchan_price', 'rtveuro_url', 'mediamarkt_url', 'mediaexpert_url')


