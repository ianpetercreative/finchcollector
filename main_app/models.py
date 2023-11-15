from django.db import models

# Create your models here.
# finches = [
#     {'name': 'Sky', 'breed': 'Zebra Finch', 'description': 'cheerful singer', 'age': 1},
#     {'name': 'Sunny', 'breed': 'Gouldian Finch', 'description': 'vibrant plumage', 'age': 2},
#     {'name': 'Pippin', 'breed': 'Java Sparrow', 'description': 'playful and social', 'age': 1},
# ]

class Finch(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

    def __str__(self):
        return self.name 