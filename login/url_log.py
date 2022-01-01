from django.conf.urls import url
from login import views
urlpatterns = [

    url('^$',views.log,name='log'),
    url(r'android/',views.Loginview.as_view()),
]
