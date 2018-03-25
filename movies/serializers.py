from .models import Movie, Person
from rest_framework import serializers


# class MovieSerializer(serializers.HyperlinkedModelSerializer):
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["id", "title", "director", "year"]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["id", "name", "surname"]