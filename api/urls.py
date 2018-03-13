from django.conf.urls import url, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')
router.register(r'projects', ProjectViewSet, 'projects')
router.register(r'work', JobViewSet, 'work')
router.register(r'links', LinkViewSet, 'links')
router.register(r'experiences', ExperienceViewSet, 'experiences')
router.register(r'skills', SkillViewSet, 'skills')
router.register(r'certificates', CertificateViewSet, 'certificates')

urlpatterns = [
  url(r'^', include(router.urls)),
  url(r'^auth/', include('rest_framework.urls')),
  url(r'^rest-auth/', include('rest_auth.urls')),
  url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
  # url(r'^rest-auth/token/', obtain_jwt_token),
  # url(r'^rest-auth/refresh/', refresh_jwt_token),
]
