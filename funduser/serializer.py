from rest_framework import serializers
from funduser.models import Fundtouser

class Fundtouserserializer(serializers.ModelSerializer):
    class Meta:
        model = Fundtouser
        fields = '__all__'