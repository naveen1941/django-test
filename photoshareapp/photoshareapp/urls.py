from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required as auth
from django.conf.urls import handler404

from photo.views import  PhotoCreateView, PhotoDetail, UserDetail, HomePageView, error404
from django.contrib.auth.decorators import login_required as auth


urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),

    url(r'^$',HomePageView,name='home' ),
    url("^login/$", "django.contrib.auth.views.login", name="login"),
    url("^logout/$", "django.contrib.auth.views.logout_then_login",name="logout"),
    url(r'^accounts/', include("registration.backends.simple.urls")),
    url(r'^photo/create/$', auth(PhotoCreateView.as_view()),name='photo_create'),
    url(r'^photo/(?P<pk>\d+)/$', PhotoDetail,name='photo_detail'),
    url(r'^photo/commentsapp/', include('django.contrib.comments.urls')),
    url(r'^users/(?P<pk>\w+)/$',  UserDetail,name='user_detail_name'),
    url(r'^users/(?P<pk>\d+)/$', UserDetail,name='user_detail'),
)
handler404 = error404