# Generated by Django 4.0.4 on 2022-06-10 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]