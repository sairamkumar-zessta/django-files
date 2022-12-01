# Generated by Django 4.1 on 2022-09-08 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('fathername', models.CharField(max_length=1000)),
                ('classname', models.IntegerField()),
                ('address', models.TextField()),
                ('dateofbirth', models.DateField(null=True)),
            ],
        ),
    ]
