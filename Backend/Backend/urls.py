from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Backend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^student/', include('student.urls')),
    url(r'^module/', include('module.urls')),
    url(r'^skill/', include('skill.urls')),
    url(r'^extra_curricular/', include('extra_curricular.urls')),
    url(r'^alumni/', include('alumni.urls')),

    
    # user auth urls
    url(r'^accounts/login/$', 'Backend.views.user_login'),
    url(r'^accounts/auth/$', 'Backend.views.auth_view'),
    url(r'^accounts/logout/$', 'Backend.views.logout'),
    url(r'^accounts/loggedin/$', 'Backend.views.loggedin'),
    url(r'^accounts/invalid/$', 'Backend.views.invalid_login'),
)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
        
if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
