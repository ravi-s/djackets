# Generated by Django 4.0.3 on 2022-03-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255), max_length=100),
        ),
    ]
