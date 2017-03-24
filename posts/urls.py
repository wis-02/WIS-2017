from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^model/$', views.getposts_from_model, name='modelposts'),
        url(r'^new/', views.post_form,),
]
