from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):
    name = models.CharField(max_length=100)
    description =models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.CharField(max_length=500, default='https://www.svgrepo.com/show/66980/fast-food-placeholder.svg')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    