from django.conf.urls import url
from xray_age import views
app_name = 'xray_Age'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.update_profile),
    url(r'^account/logout/$', views.Logout),
    url(r'^upload/$', views.upload),
]