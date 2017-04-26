"""mydc_backoffice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^films/', 'mydc.views.films', name='films'),
    url(r'^film/(?P<id>\S+)/$', 'mydc.views.film', name='film'),
    url(r'^series/', 'mydc.views.series', name='series'),
    url(r'^catalogues/', 'mydc.views.catalogues', name='catalogues'),
    url(r'^catalogue/(?P<id>\S+)/$', 'mydc.views.catalogue', name='catalogue'),
    url(r'^home/', 'mydc.views.home', name='home'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^', 'mydc.views.home'),
]
