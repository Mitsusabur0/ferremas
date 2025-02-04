# Generated by Django 5.0.7 on 2024-07-16 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name_plural': 'Shipping Address'},
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address1',
            new_name='shipping_address1',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address2',
            new_name='shipping_address2',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='shipping_city',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='full_name',
            new_name='shipping_full_name',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='shipping_state',
        ),
    ]
