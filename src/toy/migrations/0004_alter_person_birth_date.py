# Generated by Django 4.1.3 on 2023-03-12 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy', '0003_auto_20220611_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
