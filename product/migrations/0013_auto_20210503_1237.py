# Generated by Django 3.1.7 on 2021-05-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_itemdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcategories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]