from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.shortcuts import render

from users.models import CastomUser, Profile
from users.serializers import UsersSerializer, ProfileSerializer


# Create your views here.
class UsersWiewSet(viewsets.ModelViewSet):
    queryset=CastomUser.objects.all()
    serializer_class=UsersSerializer

    def put(self,request, *args,**kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response ({'error':'error'})
        try:
            instance = CastomUser.objects.get(pk=pk)
        except:
            return Response ({'error':'obj not find'})
        
        serializer = UsersSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response({'post':serializer.data})
    
   

class ProfileView(viewsets.ModelViewSet):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes = (IsAuthenticated)
    @action(methods=['get'], detail=False)
    def get(self, request):
        user = self.request.user
        queryset = get_object_or_404(Profile, id=user.id)
        serializer = ProfileSerializer(queryset)
        return Response(serializer.data)