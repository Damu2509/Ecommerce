# Generated by Django 3.1.7 on 2021-04-29 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20210429_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcategories',
            name='image',
            field=models.ImageField(default='mine1.jpg', upload_to='static'),
        ),
    ]