# Generated by Django 4.2.8 on 2024-12-30 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_coursetitle_customer_reservedcourse_delete_coupon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='register_date',
            new_name='create_date',
        ),
    ]
