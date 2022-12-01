# Generated by Django 4.1 on 2022-09-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('class_name', models.IntegerField()),
                ('date_of_birth', models.DateField()),
                ('age', models.IntegerField(editable=False)),
            ],
        ),
    ]
