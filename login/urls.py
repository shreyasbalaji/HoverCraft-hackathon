from django.conf.urls import patterns, url
from django.contrib import admin


# from django.http import HttpResponse

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hovercraft.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^new', 'login.views.new', name='new'),
    url(r'^create', 'login.views.create', name='create'),
    url(r'^view', 'login.views.view', name='view'),
    url(r'^signin', 'login.views.signin', name='signin'),
    url(r'^validate', 'login.views.validateSignIn', name='validate'),
    url(r'^logout', 'login.views.logout', name='logout'),
)