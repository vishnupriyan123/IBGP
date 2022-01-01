from rest_framework import serializers
from fund.models import Fund

class Fundserializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = '__all__'