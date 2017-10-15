from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^char_viewer/', include('character_viewer.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
