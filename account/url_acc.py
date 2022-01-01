from django.conf.urls import url
from account import views
urlpatterns = [

    url('^$',views.account,name='account'),
    url(r'android/',views.Accountview.as_view()),
]
