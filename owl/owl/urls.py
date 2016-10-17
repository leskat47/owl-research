from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^research/', include('research.urls')),
    url(r'^admin/', admin.site.urls),

]
