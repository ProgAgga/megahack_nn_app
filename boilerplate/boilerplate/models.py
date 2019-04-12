from django.db import models as md
from django.contrib.postgres import fields as pg


class SexChoices:
    MALE = 'M'
    FEMALE = 'F'
    NONBINARY = 'NB'
    CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (NONBINARY, 'Nonbinary')
    )


class Client(md.Model):
    name = md.CharField(max_length=100, null=False)
    date_of_admission = md.DateTimeField(auto_now=True)
    sex = md.CharField(max_length=100, null=True, choices=SexChoices.CHOICES)
    phone = md.CharField(max_length=10, null=False)
    age = md.IntegerField(null=False)


# Акция, которую предлагают абоненту
class Offer(md.Model):
    name = md.CharField(max_length=100, null=False, unique=True)
    due_date = md.DateTimeField(auto_now=True)
    options = pg.JSONField(null=True)


# Критерии по которым определяется подходит ли акция абоненту
class Options(md.Model):
    options = pg.JSONField(null=False)


# Диллер, продающий симкарты и предлагающий акции
class Dealer(md.Model):
    name = md.CharField(max_length=100, null=False, unique=True)


class OfferOrderResultChoices:
    SUCCESS = 'Success'
    FAIL = 'Fail'
    PENDING = 'Pending'
    CHOICES = (
        (SUCCESS, 'S'),
        (FAIL, 'F'),
        (PENDING, 'P')
    )


class OfferOrder(md.Model):
    result = md.CharField(max_length=3, choices=OfferOrderResultChoices.CHOICES)
