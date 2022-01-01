"""ibgp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^login/',include('login.url_log')),
    url('^fduser/',include('funduser.url_fuser')),
    url('^fundd/',include('fund.url_fund')),
    url('^fback/',include('feedback.url_feed')),
    url('^account/',include('account.url_acc')),
    url('^corporation/',include('corporation.url_corp')),
    url('^info/',include('info.url_info')),
    url('^request/',include('request.url_req')),
    url('^transfer/', include('transfer.url_trans')),
    url('^users/', include('users.url_user')),
    url('^reg/', include('register.url_reg')),

]



urlpatterns+=staticfiles_urlpatterns()

