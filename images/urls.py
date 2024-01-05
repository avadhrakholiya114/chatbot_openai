from django.urls import path
from .views import *

urlpatterns = [
    path("", image_genrate, name='image_genrate'),
]
