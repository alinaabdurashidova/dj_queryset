# Generated by Django 5.0 on 2023-12-17 13:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OnetoOneApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='capital_city',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='countries', related_query_name='country', to='OnetoOneApp.capitalcity'),
        ),
    ]