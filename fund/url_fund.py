from django.conf.urls import url
from fund import views
urlpatterns = [

    url('^$',views.fund,name='fund'),
    url(r'android/',views.Fundview.as_view()),
    url('^ad/', views.fn, name="fn"),
]
