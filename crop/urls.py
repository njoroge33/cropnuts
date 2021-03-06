from django.urls import path, re_path, include
from .views import UserList, ListCrate, SampleList
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api/users', UserList)
router.register(r'api/crates', ListCrate)
router.register(r'api/samples', SampleList)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('api/login', views.login, name='login'),
]
