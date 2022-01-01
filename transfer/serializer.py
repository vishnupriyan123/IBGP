from rest_framework import serializers
from transfer.models import Transfer

class Transferserializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'