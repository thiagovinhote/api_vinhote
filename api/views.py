from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, pagination, generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import *

class UserViewSet(viewsets.ModelViewSet):
  
  queryset = User.objects.all()
  serializer_class = UserSerializer


class DefaultPagination(pagination.PageNumberPagination):
  page_size = 4


class ProjectViewSet(viewsets.ModelViewSet):

  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  pagination_class = DefaultPagination


class JobViewSet(viewsets.ModelViewSet):

  queryset = Job.objects.all()
  serializer_class = JobSerializer
  filter_backends = (DjangoFilterBackend,)
  filter_fields = ('name', 'is_store')


class LinkViewSet(viewsets.ModelViewSet):

  queryset = Link.objects.all()
  serializer_class = LinkSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
  
  queryset = Experience.objects.all()
  serializer_class = ExperienceSerializer


class SkillViewSet(viewsets.ModelViewSet):
  
  queryset = Skill.objects.all()
  serializer_class = SkillSerializer


class CertificateViewSet(viewsets.ModelViewSet):

  queryset = Certificate.objects.all()
  serializer_class = CertificateSerializer