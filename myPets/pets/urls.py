from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PetsViewSet 
app_name='pets'

router = DefaultRouter()

router.register('pets', PetsViewSet)

urlpatterns = [
    path('',include(router.urls)),
]