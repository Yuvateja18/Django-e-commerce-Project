# Generated by Django 5.2.1 on 2025-06-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstApp", "0004_products"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="img"),
        ),
    ]
