from rest_framework import serializers
from register.models import Register

class Registerserializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'