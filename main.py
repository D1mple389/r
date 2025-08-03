from setup import *
from django.db import models


class Role(models.Mode):
    name = models.CharField(max_lenght=50)


class User(models.Mode):
    title = models.CharField(max_lenght=100)
    email = models.EmailField(max_lenght=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

