# Generated by Django 5.1 on 2024-10-09 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_expiry_system', '0003_remove_product_name_product_barcode_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='barcode_data',
        ),
        migrations.RemoveField(
            model_name='product',
            name='barcode_image',
        ),
    ]
