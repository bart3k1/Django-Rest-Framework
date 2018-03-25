from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)

    def __str__(self):
        return self.name + " - " + self.surname


class Movie(models.Model):
    title = models.CharField(max_length=64, verbose_name="Tytuł")
    director = models.ForeignKey(Person, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Person, related_name="persons", through="Role")
    year = models.IntegerField()

    def __str__(self):
        return self.title


class Role(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role_name = models.CharField(max_length=128)
