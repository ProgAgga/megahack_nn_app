from rest_framework import serializers as sz

from boilerplate.models import *


class ClientSerializer(sz.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'sex', 'phone', 'age', 'date_of_admission')


class OfferSerializer(sz.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'name', 'due_date', 'options')


class DealerSerializer(sz.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ('id', 'name')

