from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cat(models.Model):
    color = models.CharField(choices=(('black', 'black'), ('white', 'white'), ('brown', 'brown'), ('orange', 'orange')),
                             max_length=10)
    age = models.PositiveIntegerField()
    description = models.TextField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.color} {self.breed.name}"
