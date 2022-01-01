from django.conf.urls import url
from users import views
urlpatterns = [

    url('^$',views.users,name='user'),
    url('^ar/', views.fn, name="fn"),
    url(r'android/',views.Userview.as_view()),
]
