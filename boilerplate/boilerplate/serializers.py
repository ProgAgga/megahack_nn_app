from rest_framework import serializers as sz

from boilerplate.models import *


class ClientSerializer(sz.ModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'sex', 'phone', 'age', 'date_of_admission')


