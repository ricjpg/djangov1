from django.conf.urls import url
from newApp import views 
 
urlpatterns = [ 
    url(r'^api/newApp$', views.userApi),
    url(r'^api/newApp/([0-9]+)$', views.tutorial_detail)
]