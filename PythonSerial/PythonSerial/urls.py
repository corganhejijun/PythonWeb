from django.conf.urls import include, url
from django.contrib import admin
import SerialRead.views

urlpatterns = [
    # Examples:
    # url(r'^$', 'PythonSerial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^SerialRead/json/', SerialRead.views.getJson, name='json'),
    url(r'^SerialRead/', SerialRead.views.index, name='index'),
]
