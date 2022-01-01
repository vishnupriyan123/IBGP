from django.conf.urls import url
from funduser import views
urlpatterns = [

    url('^$',views.fuser,name='fuser'),
    url(r'android/', views.Fundtouserview.as_view()),
]
