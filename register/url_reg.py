from django.conf.urls import url
from register import views
urlpatterns = [

    url('^$',views.reg,name='reg'),
    url('^vl/', views.fn, name="fn"),
    url(r'android/',views.Registerview.as_view()),
]
