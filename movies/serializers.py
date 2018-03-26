from .models import Movie, Person, Role
from rest_framework import serializers


class RoleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='person.id')
    name = serializers.CharField(source='person.name')
    surname = serializers.CharField(source='person.surname')
    movie_id = serializers.IntegerField(source='movie.id')

    class Meta:
        model = Role
        fields = ['id', 'name', 'surname', 'role_name', 'movie_id']


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

    def update(self, instance, validated_data):
        actors_data = validated_data.pop('role_set')
        movie = super().update(instance, validated_data)
        for actor_data in actors_data:
            Role.objects.update_or_create(
                person_id=actor_data['person']['id'],
                movie_id=movie.id,
                defaults={'role': actor_data['role']},
            )
        return movie