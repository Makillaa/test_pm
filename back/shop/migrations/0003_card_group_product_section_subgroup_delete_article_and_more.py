# Generated by Django 4.0.1 on 2022-01-13 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_article_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Card')),
                ('description', models.TextField(verbose_name='card description')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='group')),
                ('description', models.TextField(verbose_name='group description')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='product name')),
                ('description', models.TextField(verbose_name='product description')),
                ('scope_of_application', models.TextField(verbose_name='scope of application')),
                ('diameter', models.IntegerField(verbose_name='diameter')),
                ('length', models.FloatField(verbose_name='length')),
                ('color', models.CharField(max_length=64, verbose_name='color')),
                ('image', models.ImageField(upload_to='media/', verbose_name='image')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.card')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='category name')),
                ('description', models.TextField(verbose_name='section description')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
        migrations.CreateModel(
            name='Subgroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Subgroup')),
                ('description', models.TextField(verbose_name='subgroup description')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.group')),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='group',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.section'),
        ),
        migrations.AddField(
            model_name='card',
            name='subgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.subgroup'),
        ),
    ]
