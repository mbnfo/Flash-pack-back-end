from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FlashCard(models.Model):
    answer = models.CharField(max_length = 10000)
    question = models.CharField(max_length = 10000)
    rating = models.IntegerField(default = 5)

class FlashPacks(models.Model):
    cards = models.ManyToManyField(FlashCard)
    name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

