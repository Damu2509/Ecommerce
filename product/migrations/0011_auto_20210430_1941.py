# Generated by Django 3.1.7 on 2021-04-30 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210430_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemcategories',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]