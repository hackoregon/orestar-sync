from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path


urlpatterns = [
    path('local-elections/admin/', admin.site.urls),
    url(r'^local-elections/', include('api.urls')),
]
