from rest_framework import serializers
from corporation.models import Corporation

class Corporationserializer(serializers.ModelSerializer):
    class Meta:
        model = Corporation
        fields = '__all__'