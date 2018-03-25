from django.contrib import admin

# Register your models here.
from movies.models import Person, Movie, Role


class RoleInline(admin.TabularInline):
    model = Movie.actors.through

# class RoleInline(admin.StackedInline):
#     model = Movie.actors.through


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")
    inlines = [
        RoleInline,
    ]


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "director", "year")
    inlines = [
        RoleInline,
    ]