from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProfileView, UsersWiewSet
app_name='users'

router = DefaultRouter()

router.register('profile', ProfileView)
router.register('users', UsersWiewSet)

urlpatterns = [
    path('',include(router.urls))
]