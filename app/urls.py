from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('upload', UploadFileView)
router.register('deletion_time', ExpireTimeView)
router.register('user', UserView)

urlpatterns = [
    path('', include(router.urls)),
]
