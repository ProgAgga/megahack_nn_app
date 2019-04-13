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
    dealer = sz.PrimaryKeyRelatedField(read_only=True)
    client = sz.PrimaryKeyRelatedField(read_only=True)

    id_hash = sz.ReadOnlyField()
    status = sz.ReadOnlyField()
    date_processed = sz.ReadOnlyField()

    class Meta:
        model = OfferOrder
        fields = ('offer', 'client', 'dealer', 'id_hash', 'status', 'date_created', 'date_processed')
        extra_kwargs = {
            'id_hash': {'required': False},
            'status': {'required': False},
            'date_created': {'required': False},
            'date_processed': {'required': False}
        }


class SourceSerializer(sz.ModelSerializer):
    class Meta:
        model = Source
        fields = ('id', 'name', 'port', 'host', 'username', 'password', 'type', 'database')
