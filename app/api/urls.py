from django.conf.urls import url, include
from rest_framework import routers
from app.api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

# Use automatic URL routing. Include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]