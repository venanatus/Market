# Generated by Django 4.1.3 on 2023-05-17 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uxod_za_veshyu',
            field=models.CharField(max_length=255, null=True),
        ),
    ]