# Generated by Django 4.2.1 on 2023-07-09 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='create_on',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان دقیق ثبت'),
        ),
    ]
