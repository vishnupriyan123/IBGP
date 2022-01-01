from django.conf.urls import url
from feedback import views
urlpatterns = [

    url('^$',views.feedback,name='feedback'),
    url(r'android/',views.Feedbackview.as_view()),
]
