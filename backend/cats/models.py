from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Breed(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Cat(models.Model):
    COLOR_CHOICES = [
        ('black', 'black'),
        ('white', 'white'),
        ('brown', 'brown'),
        ('orange', 'orange'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    color = models.CharField(choices=COLOR_CHOICES,
                             max_length=10)
    age = models.PositiveIntegerField()
    description = models.TextField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name="cats")

    def __str__(self):
        return f"{self.color} {self.breed.name}"


class Rate(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField(choices=(
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ))

    class Meta:
        unique_together = ('cat', 'user')

    def __str__(self):
        return f"{self.user} has rated {self.cat} as {self.rate}"
