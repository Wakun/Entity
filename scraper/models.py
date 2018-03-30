from django.db import models


class Product(models.Model):

    art_name = models.CharField('Nazwa artykułu', max_length=255, null=True, blank=True)
    plu_num = models.IntegerField('Numer krótki', default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    auchan_price = models.FloatField('Cena Auchan', null=True, blank=True)

    rtveuro_price = models.FloatField('Cena RTVEuroAGD', null=True, blank=True)
    rtveuro_url = models.CharField('Link do RTVEuroAGD', null=True, blank=True, max_length=1000)

    mediamarkt_price = models.FloatField('Cena Media Markt', null=True, blank=True)
    mediamarkt_url = models.CharField('Link do Media Markt', null=True, blank=True, max_length=1000)

    mediaexpert_price = models.FloatField('Cena Media Expert', null=True, blank=True)
    mediaexpert_url = models.CharField('Link do Media Expert', null=True, blank=True, max_length=1000)

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'



class Category(models.Model):

    category_name = models.CharField('Kategoria', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'


