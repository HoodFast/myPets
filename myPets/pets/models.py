from django.db import models

class Category(models.Model):
    name = models.CharField('категория',max_length=100)
    description = models.TextField(blank=True)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Категория"
        verbose_name_plural="Категории"


class PetsBreeds(models.Model):
    name = models.CharField('категория',max_length=100)
    description = models.TextField(blank=True)
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Порода"
        verbose_name_plural="Породы"


class MyPets(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    owner = models.ForeignKey(
        to='users.CastomUser',
        on_delete=models.CASCADE,
        related_name='users',
        verbose_name='Хозяин',
    )
    photo = models.ImageField(upload_to='photo/',blank=True)
    video = models.FileField(upload_to='video/',blank=True)
    categories = models.ForeignKey(to='pets.Category', on_delete=models.PROTECT, null=True)
    timeCreate = models.DateTimeField(auto_now_add=True)
    timeUpdate = models.DateTimeField(auto_now=True)
    # breeds = models.ManyToManyField(PetsBreeds ,verbose_name='порода', null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="Питомец"
        verbose_name_plural="Питомцы"


class Likes(models.Model):
    ownerLikes=models.ForeignKey(
        to='users.CastomUser',
        on_delete=models.CASCADE,
        related_name='Ownlikes',
        verbose_name='Хозяин',
    )
    petsLikes = models.ForeignKey(
        to='pets.MyPets',
        on_delete=models.CASCADE,
        related_name='likes',
        verbose_name='Лайк',
    )


class Posts(models.Model):
    petsPost = models.ForeignKey(
        to='pets.MyPets',
        on_delete=models.CASCADE,
        related_name='post',
        verbose_name='Пост',
    )
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True) 
    timeCreate = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    author = models.ForeignKey(to='users.CastomUser', on_delete=models.CASCADE, related_name='author')
    post = models.ForeignKey(to='Posts',on_delete=models.CASCADE,related_name='post')
    text = models.TextField(blank=True)