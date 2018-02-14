from rest_framework import serializers
from .models import *
from .constants import LINK_TYPES

class LinkSerializer(serializers.ModelSerializer):
  
  type_display = serializers.ChoiceField(LINK_TYPES, source = 'get_type_display', read_only = True)

  class Meta:
    model = Link
    fields = '__all__'

class LinkSimpleSerializer(LinkSerializer):
  
  class Meta:
    model = Link
    fields = ('id', 'url', 'type_display')

class ProjectSerializer(serializers.ModelSerializer):
  
  links = LinkSimpleSerializer(many = True, read_only = True)

  class Meta:
    model = Project
    fields = '__all__'

class JobSerializer(serializers.ModelSerializer):

  class Meta:
    model = Job
    fields = '__all__'