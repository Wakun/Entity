# Generated by Django 2.0.3 on 2018-04-02 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0002_auto_20180331_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='auchan_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nazwa Auchan'),
        ),
    ]
