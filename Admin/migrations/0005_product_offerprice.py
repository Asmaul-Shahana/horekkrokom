# Generated by Django 4.1.1 on 2024-02-23 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_product_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offerPrice',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
