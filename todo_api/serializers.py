from rest_framework import serializers
from .models import Todo

class doSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['task','timestamp','completed','updated','user']

