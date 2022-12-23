from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from db.views import *
from rest_framework import routers
app_name = 'glossary'


urlpatterns = [
    # Получение всех объектов
    path('glossary/view/all/', GlossaryListView.as_view()),
    # Добавление нового объекта
    path('glossary/create/', GlossaryListView.as_view()),
    # Изменение и удаление
    path('glossary/detail/<int:pk>/', GlossaryAPIDetail.as_view()),

    # favouriteGlossies

    # Получение всех объектов
    path('favouriteGlossary/view/all/', FavouriteGlossaryViewSet.as_view()),
    # Добавление нового объекта
    path('favouriteGlossary/create/', FavouriteGlossaryViewSet.as_view()),
    # Изменение и удаление
    path('favouriteGlossary/detail/<int:pk>/',
         FavouriteGlossaryAPIDetail.as_view()),


]

# ! for to save images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
