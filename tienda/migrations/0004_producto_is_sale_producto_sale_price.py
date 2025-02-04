# Generated by Django 5.0.7 on 2024-07-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_remove_producto_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producto',
            name='sale_price',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10),
        ),
    ]
