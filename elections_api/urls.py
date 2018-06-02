from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Hack Oregon 2018 Local Elections APIs')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('api.urls')),
    url(r'^local-elections/$', schema_view),
]
