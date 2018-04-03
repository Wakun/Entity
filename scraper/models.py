from django.db import models

from django.core.validators import URLValidator, ValidationError

class Product(models.Model):

    art_name = models.CharField('Nazwa artykułu', max_length=255, null=True, blank=True, unique=True)
    auchan_name = models.CharField('Nazwa Auchan', max_length=255, null=True, blank=True, unique=True)
    plu_num = models.IntegerField('Numer krótki', default=0, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    auchan_price = models.FloatField('Cena Auchan', null=True, blank=True)

    rtveuro_price = models.FloatField('Cena RTVEuroAGD', null=True, blank=True)
    rtveuro_url = models.CharField('Link do RTVEuroAGD', null=True, blank=True, max_length=1000, unique=True)
    rtveuro_url_valid = models.BooleanField(default=False)


    mediamarkt_price = models.FloatField('Cena Media Markt', null=True, blank=True)
    mediamarkt_url = models.CharField('Link do Media Markt', null=True, blank=True, max_length=1000, unique=True)
    mediamarkt_url_valid = models.BooleanField(default=False)


    mediaexpert_price = models.FloatField('Cena Media Expert', null=True, blank=True)
    mediaexpert_url = models.CharField('Link do Media Expert', null=True, blank=True, max_length=1000, unique=True)
    mediaexpert_url_valid = models.BooleanField(default=False)


    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'


    def save(self, *args, **kwargs):

        if self.is_rtv_url_valid():
            self.rtveuro_url_valid = True
        else:
            self.rtveuro_url_valid = False
            self.rtveuro_url = None

        if self.is_mm_url_valid():
            self.mediamarkt_url_valid = True
        else:
            self.mediamarkt_url_valid = False
            self.mediamarkt_url = None

        if self.is_me_url_valid():
            self.mediaexpert_url_valid = True
        else:
            self.mediaexpert_url_valid = False
            self.mediaexpert_url = None

        super(Product, self).save(*args, **kwargs)

    def is_rtv_url_valid(self):

        try:
            validate = URLValidator()
            if self.rtveuro_url:
                validate(self.rtveuro_url)
                return True
            else:
                return False
        except (ValueError, ValidationError):
            return False

    def is_mm_url_valid(self):

        try:
            validate = URLValidator()
            if self.mediamarkt_url:
                validate(self.mediamarkt_url)
                return True
            else:
                return False
        except (ValueError, ValidationError):
            return False

    def is_me_url_valid(self):

        try:
            validate = URLValidator()
            if self.mediaexpert_url:
                validate(self.mediaexpert_url)
                return True
            else:
                return False
        except (ValueError, ValidationError):
            return False


class Category(models.Model):

    category_name = models.CharField('Kategoria', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'


