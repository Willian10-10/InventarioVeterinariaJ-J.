# Generated by Django 5.0.1 on 2024-12-01 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestorProductos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
