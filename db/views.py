
from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from db.serializers import GlossarySerializer
from .models import Glossary
from rest_framework.permissions import *
# Create your views here.


# class PersonViewSet(viewsets.ModelViewSet):
#     queryset = Person.objects.all()
#     serializer_class = PersonSerializer

class GlossaryListView(generics.ListCreateAPIView):
    queryset = Glossary.objects.all()
    serializer_class = GlossarySerializer



class GlossaryAPIDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Glossary.objects.all()
    serializer_class = GlossarySerializer




# class PersonView(APIView):
#     def get (self, request): # GET запрос показать всех объектов
#         person = Person.objects.all() #Получение всех объектов с БД
#         serializer = PersonSerializer(person, many=True)
        
#         return Response ({
#             "person":serializer.data
#         })

#     def post(self, request):# POST запрос добавление нового объекта
#         persons = request.data
#         serializer = PersonSerializer(data=persons)
#         if serializer.is_valid(raise_exception=True):
#                 persons_saved = serializer.save()
#         return Response({"Готово":"Люди '{}' добавлен успешно.".format(persons_saved.name)})
          
#     def put(self,request, *args, **kwargs ):# PUT запрос изменение объекта
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"Ошибка":"Не найдено ID"})
#         try:
#             instance = Person.objects.get(pk=pk)
#         except:
#             return Response({"Ошибка":"Не найдено объект"})
        
#         serializers = PersonSerializer(data=request.data, instance=instance)
#         serializers.is_valid(raise_exception=True)
#         serializers.save()
#         return Response({"Изменен": serializers.data})
#     def delete(self, request, pk):# DELETE запрос удаление объекта

#         person = get_object_or_404(Person.objects.all(), pk=pk)
#         person.delete()
#         return Response({
#          "Сообщение": "Этот человек `{}` удален.".format(pk)
#      }, status=204)
