from django.conf.urls import url, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, 'projects')
router.register(r'work', JobViewSet, 'work')
router.register(r'links', LinkViewSet, 'links')

urlpatterns = [
  url(r'^', include(router.urls)),
]
