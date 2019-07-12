from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view


router = DefaultRouter()
router.register(r'oreStarData', views.oreStarDetailViewSet)

schema_view = get_swagger_view(title='Hack Oregon 2018 Local Elections APIs')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'contributorgraph', views.graph),
    url(r'^', include(router.urls)),
]
