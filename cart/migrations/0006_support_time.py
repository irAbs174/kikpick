# Generated by Django 4.2.1 on 2023-07-11 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_cart_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='support',
            name='time',
            field=models.TextField(blank=True, null=True),
        ),
    ]
