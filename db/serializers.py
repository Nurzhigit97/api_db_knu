
from dataclasses import fields
from rest_framework import serializers

from db.models import  Glossary



class GlossarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Glossary
        fields = "__all__"


    # name = serializers.CharField(max_length = 20)
    # firstName = serializers.CharField(max_length = 50)
    # birthday = serializers.DateField()
    # male = serializers.CharField(max_length = 20)

    # def create(self, validated_data):
    #     return Person.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.firstName = validated_data.get('firstName', instance.firstName)
    #     instance.birthday = validated_data.get('birthday', instance.birthday)
    #     instance.male = validated_data.get('male', instance.male)
    #     instance.save()
    #     return instance
