# Generated by Django 4.1.1 on 2024-02-22 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0004_indorder_date_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indorder',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
