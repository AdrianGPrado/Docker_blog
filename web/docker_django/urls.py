from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # URL per django app
    url(r'^', include('docker_django.apps.todo.urls')),
]
