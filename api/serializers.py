from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from .constants import LINK_TYPES

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    extra_kwargs = {
      'password': {'write_only': True}
    }


class UserSerializerAuth(UserSerializer):
  
  class Meta:
    model = User
    fields = (
      'id',
      'username',
      'first_name',
      'last_name',
      'email',
      'is_superuser',
      'is_active',
      'avatar',
    )
    extra_kwargs = {
      'password': {'write_only': True}
    }


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


class ExperienceSerializer(serializers.ModelSerializer):
  
  days_time = serializers.IntegerField(read_only = True)

  class Meta:
    model = Experience
    fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Skill
    fields = '__all__'


class CertificateSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Certificate
    fields = '__all__'
