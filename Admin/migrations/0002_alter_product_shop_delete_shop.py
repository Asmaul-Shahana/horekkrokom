# Generated by Django 4.1.1 on 2024-02-12 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Search', '0004_rename_ownerid_owner_shopid_owner_shopname'),
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Search.owner'),
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
