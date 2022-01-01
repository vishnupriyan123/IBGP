from django.conf.urls import url
from info import views
urlpatterns = [

    url('^$',views.info,name='info'),
    url(r'android/',views.Infoview.as_view()),
]
