from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # URL per django app
    # url(r'^', include('docker_django.apps.todo.urls')),

    url(r'^$', 'docker_django.apps.todo.views.home', name='home'),

    url(r'^home/$', 'docker_django.apps.todo.views.home', name='home'),

    url(r'^about/$', 'docker_django.apps.todo.views.about', name='about'),

    url(r'^contact/$', 'docker_django.apps.todo.views.contact', name='contact'),

]
