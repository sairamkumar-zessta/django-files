# Generated by Django 4.1 on 2022-09-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_alter_details_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='age',
            field=models.IntegerField(blank=True, editable=False),
        ),
    ]
