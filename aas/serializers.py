from rest_framework import serializers
from .models import aasItem


class aasSerializer(serializers.ModelSerializer):

    class Meta:
        model = aasItem
        fields = '__all__'