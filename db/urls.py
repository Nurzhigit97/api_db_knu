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

    # Получение всех объектов добавленных от пользователей
    path('addedGlossaryByUser/view/all/', CheckGlossaryListView.as_view()),
    # Добавление нового объекта добавленных от пользователей
    path('addedGlossaryByUser/create/', CheckGlossaryListView.as_view()),
    # Изменение и удаление глоссария от пользователей
    path('addedGlossaryByUser/detail/<int:pk>/', CheckGlossaryAPIDetail.as_view()),

]

# ! for to save images
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
