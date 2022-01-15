from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='category name', max_length=128)
    description = models.TextField(verbose_name='category description')

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(verbose_name='category name', max_length=128)
    description = models.TextField(verbose_name='section description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(verbose_name='group', max_length=128)
    description = models.TextField(verbose_name='group description')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='section')

    def __str__(self):
        return self.name


class Subgroup(models.Model):
    name = models.CharField(verbose_name='Subgroup', max_length=128)
    description = models.TextField(verbose_name='subgroup description')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='group')

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(verbose_name='Card', max_length=128)
    description = models.TextField(verbose_name='card description')
    subgroup = models.ForeignKey(Subgroup, on_delete=models.CASCADE, related_name='subgroup')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(verbose_name='product name', max_length=128)
    description = models.TextField(verbose_name='product description')
    scope_of_application = models.TextField(verbose_name='scope of application')
    diameter = models.FloatField(verbose_name='diameter')
    length = models.IntegerField(verbose_name='length')
    color = models.CharField(verbose_name='color', max_length=64)
    image = models.ImageField(verbose_name='image', upload_to='media/')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='card')

    def __str__(self):
        return self.name
