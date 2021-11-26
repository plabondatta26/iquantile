from .serializers import *
from rest_framework import viewsets
from django.shortcuts import render, redirect


# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UploadFileView(viewsets.ModelViewSet):
    queryset = UploadFileModel.objects.all()
    serializer_class = UploadFileSerializer

    def get(self, request):
        return self.queryset.filter(user=request.user.id).order_by('-id')


class ExpireTimeView(viewsets.ModelViewSet):
    queryset = ExpireTime.objects.all()
    serializer_class = ExpireTimeSerializer

    def get(self, request):
        return self.queryset.filter(user=request.user.id).order_by('-id')

