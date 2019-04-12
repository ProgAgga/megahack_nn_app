from django.db import models
from django.contrib.postgres import fields as pg


class Client(models.Model):
    name = models.CharField(max_length=100, null=False)
    date_of_admission = models.DateTimeField(auto_now=True)
    sex = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=10, null=False)
    age = models.IntegerField(null=False)


# Акция, которую предлагают абоненту
class Offer(models.Model):
    name = models.CharField(max_length=100, null=False)
    due_date = models.DateTimeField(auto_now=True)
    options = pg.JSONField(null=True)


# Критерии по которым определяется подходит ли акция абоненту
class Options(models.Model):
    options = pg.JSONField(null=False)


# Диллер, продающий симкарты и предлагающий акции
class Dealer(models.Model):
    name = models.CharField(max_length=100, null=False)



