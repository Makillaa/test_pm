# Generated by Django 4.0.1 on 2022-01-13 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_card_group_product_section_subgroup_delete_article_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='diameter',
            field=models.FloatField(verbose_name='diameter'),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.IntegerField(verbose_name='length'),
        ),
    ]
