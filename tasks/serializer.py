from rest_framework import serializers
from .models import Task

class Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title', 'pub_date', 'description'] 