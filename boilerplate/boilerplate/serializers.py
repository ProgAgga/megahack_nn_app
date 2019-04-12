from rest_framework import serializers as sz

from boilerplate.models import *


class ClientSerializer(sz.ModelSerializer):
    dealer = sz.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Client
        fields = ('id', 'name', 'sex', 'phone', 'age', 'date_of_admission', 'dealer')


class OfferSerializer(sz.ModelSerializer):
    class Meta:
        model = Offer
        fields = ('id', 'name', 'due_date', 'options')


class DealerSerializer(sz.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ('id', 'name')


class OfferOrderSerializer(sz.ModelSerializer):
    offer = sz.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = OfferOrder
        fields = ('offer', 'result', 'date_created', 'date_processed', 'id_hash')
