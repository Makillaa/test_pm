from rest_framework import serializers
from . import models


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name', 'description']


