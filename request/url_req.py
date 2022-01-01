from django.conf.urls import url
from request import views
urlpatterns = [

    url('^$',views.req,name='req'),
    url('^tf/', views.fn, name="fn"),
    url('^st/', views.gn, name="gn"),
    url(r'android/',views.Requestview.as_view()),
]
