from django.contrib.auth.models import User
from rest_framework import serializers
from app.models import Place


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email',)

class PlaceSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Place
        fields = ('url','user', 'title', 'description','photo','by',)
