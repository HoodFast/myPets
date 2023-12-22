from rest_framework import serializers

from .models import (MyPets,Likes,Posts)


class PostsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Posts
        fields='__all__'


class LikesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Likes
        fields=('ownerLikes',)

class MyPetsListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MyPets
        fields = ('name' , 'owner','id')


class MyPetsDetailSerializer(serializers.ModelSerializer):
    
    likes = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()
    class Meta:
        model = MyPets
        fields = '__all__'

    def get_likes(self,obj):
        queryset = Likes.objects.filter(petsLikes=obj.id).all()
        serializer = LikesSerializer(queryset, many=True)
        return serializer.data
       
    def get_posts(self,obj):
        queryset = Posts.objects.filter(petsPost=obj.id).all()
        serializer = PostsSerializer(queryset, many=True)
        return serializer.data   