from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, PlaceSerializer
from app.models import Place

from app.api.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint that only allows GET, OPTIONS
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class PlaceViewSet(viewsets.ModelViewSet):
    """
    Endpoint that allows GET, PUT, PATCH, DELETE, OPTIONS
    """
    queryset = Place.objects.all().order_by('title')
    serializer_class = PlaceSerializer

    # set the user(field user) that created the place
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)