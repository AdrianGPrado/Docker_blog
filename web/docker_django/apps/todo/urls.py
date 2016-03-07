from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    # Admin

    url(r'^$', views.home, name='home'),

    url(r'^home/$', 'docker_django.apps.todo.urls.views.home', name='home'),

    url(r'^about/$', 'docker_django.apps.todo.urls.views.about', name='about'),

    url(r'^contact/$', 'docker_django.apps.todo.urls.views.contact', name='contact'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
