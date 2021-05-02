# Generated by Django 3.1.7 on 2021-05-01 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20210430_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=1000)),
                ('tag', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0.0)),
                ('discount', models.FloatField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]