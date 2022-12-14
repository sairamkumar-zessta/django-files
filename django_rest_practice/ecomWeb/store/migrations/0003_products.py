# Generated by Django 4.1 on 2022-09-26 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('brand', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('cart', models.ManyToManyField(to='store.cart')),
            ],
        ),
    ]
