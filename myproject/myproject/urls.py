from django.conf.urls import include, url, patterns
from django.contrib import admin

from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', 'cmsput.views.barra'),
    url(r'^accounts/profile/$','cmsput.views.pages'),
    url(r'^pages/(\d+)$', 'cmsput.views.pages'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login', login),
    url(r'^logout', logout),
)
