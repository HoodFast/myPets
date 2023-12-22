from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import MyPets
from .serializers import MyPetsListSerializer, MyPetsDetailSerializer



class PetsViewSet(ModelViewSet):
    queryset = MyPets.objects.all()
    serializer_class = MyPetsListSerializer
   

