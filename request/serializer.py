from rest_framework import serializers
from request.models import Request

class Requestserializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'