# Generated by Django 2.0.3 on 2018-04-04 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_auto_20180403_0150'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='dyskonty/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
