from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(MyPets)
admin.site.register(Likes)
admin.site.register(Posts)
admin.site.register(Comment)