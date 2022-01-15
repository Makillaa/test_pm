from django.urls import path
from . import views

urlpatterns = [
    path('category/all/', views.CategoryListView.as_view()),  # Список категорий
    path('category/info/<int:id>', views.CategoryInfoView.as_view()),  # Список всех карточек товаров категории
    path('card/info/<int:id>', views.CardDetailInfo.as_view()),  # Детальная информация о карточке
    path('prodincard/<int:id>', views.ListProdInCard.as_view())  # Список продуктов по определенной карточке
]