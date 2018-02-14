from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *

class ProjectViewSet(viewsets.ModelViewSet):

  queryset = Project.objects.all()
  serializer_class = ProjectSerializer


class JobViewSet(viewsets.ModelViewSet):

  queryset = Job.objects.all()
  serializer_class = JobSerializer


class LinkViewSet(viewsets.ModelViewSet):

  queryset = Link.objects.all()
  serializer_class = LinkSerializer
