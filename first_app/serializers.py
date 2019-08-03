from rest_framework import serializers
from .models import blog , profile
from django.contrib.auth.models import User

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model=blog
        fields='__all__'


class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model=profile
        fields='__all__'

    