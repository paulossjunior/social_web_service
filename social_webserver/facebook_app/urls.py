from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from facebook_app import views

urlpatterns = [
    url(r'^me/(?P<pk>[0-9]+)$', views.Facebook_User.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
