# Generated by Django 5.0.6 on 2024-06-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_category_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularpizza',
            name='category_description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='sicilianpizza',
            name='category_description',
            field=models.CharField(max_length=500),
        ),
    ]