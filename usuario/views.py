from urllib import request
from django.shortcuts import render
from usuario.models import UsuarioModel
from perfil.models import Perfil

from usuario.serializers import UsuarioSerializer
from rest_framework import viewsets

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = UsuarioModel.objects.all()
    http_method_names = ['get', 'post', 'patch']