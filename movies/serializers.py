from .models import Movie, Person, Role
from rest_framework import serializers


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='person.id')
    name = serializers.CharField(source='person.name')
    movie_id = serializers.IntegerField(source='movie.id')

    class Meta:
        model = Role
        fields = ['id', 'name', 'role_name', 'movie_id']


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ["id", "name", "surname"]


class MovieSerializer(serializers.ModelSerializer):
    # actors = PersonSerializer(many=True, read_only=True)
    actors = RoleSerializer(many=True, source='role_set')
    director = PersonSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "director", "year", "actors"]