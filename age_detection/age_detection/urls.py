from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from xray_age import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xray_age/', include('xray_age.urls')),
    url(r'^account/', include('social_django.urls', namespace='social')),
    url(r'^account/', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)