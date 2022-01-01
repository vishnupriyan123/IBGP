from django.conf.urls import url
from corporation import views
urlpatterns = [

    url('^$',views.corporation,name='corporation'),
    url('^vl/', views.fn, name="fn"),
    url('^up/(?P<cid>\w+)', views.up, name="up"),
    url('^de/(?P<cid>\w+)', views.de, name="de"),
    url(r'android/',views.Corporationview.as_view()),

]