from django.conf.urls import url
from transfer import views
urlpatterns = [

    url('^$',views.trans,name='trans'),
    url(r'android/',views.Transferview.as_view()),
]
