from rest_framework import serializers
from info.models import Info

class Infoserializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'