from rest_framework import generics
from . import serializers, models
from rest_framework.views import APIView
from rest_framework.response import Response


# Список категорий
class CategoryListView(generics.ListAPIView):
    serializer_class = serializers.CategoryDetailSerializer
    queryset = models.Category.objects.all()


# Список всех карточек товаров категории
class CategoryInfoView(APIView):
    def get(self, request, id):
        cards = models.Card.objects.filter(subgroup__group__section__category=id).values('id', 'name', 'description')
        list_cards = []

        for i in cards:
            list_cards.append(i)

        return Response({'data': list_cards})


# Детальная информация о карточке
class CardDetailInfo(APIView):
    def get(self, request, id):
        cards = models.Card.objects.filter(id=id).values('name')
        products = models.Product.objects.filter(card_id=id)\
            .values('name', 'scope_of_application', 'diameter', 'length', 'color', 'image')
        finish_lib = {'card_name': None, 'product_names': [], 'diameter': [], 'length': [], 'colors': [], 'images': []}

        for card in cards:
            finish_lib['card_name'] = card['name']

        for product in products:
            finish_lib['product_names'].append(product['name'])
            if not product['diameter'] in finish_lib['diameter']:
                finish_lib['diameter'].append(product['diameter'])
            if not product['length'] in finish_lib['length']:
                finish_lib['length'].append(product['length'])
            if not product['color'] in finish_lib['colors']:
                finish_lib['colors'].append(product['color'])
            finish_lib['images'].append(product['image'])

        return Response({'data': finish_lib})


# Список продуктов по определенной карточке
class ListProdInCard(APIView):
    def get(self, request, id):
        cards = models.Card.objects.filter(id=id).values('name')
        products = models.Product.objects.filter(card_id=id).values('name')
        result = {'card': None, 'products': []}

        for card in cards:
            result['card'] = card['name']

        for product in products:
            result['products'].append(product['name'])

        return Response({'data': result})
