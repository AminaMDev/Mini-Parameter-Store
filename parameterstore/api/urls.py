from django.urls import include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from .views import ParameterViewSet

schema_view = get_swagger_view(title='Parameter Store API')

router = DefaultRouter()
router.register('parameter', ParameterViewSet)

urlpatterns = [
    re_path('^$', schema_view),
    re_path('^api/', include(router.urls)),
]
