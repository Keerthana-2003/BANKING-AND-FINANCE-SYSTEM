"""banking URL Configuration

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
from django.contrib import admin
from django.urls import path
from myapp.views import *
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.home, name="index"),
    path('login/',views.login1, name='login'),
    path('signup/',views.signup),
    path('',views.landing),
    path('contact/',views.contact),
    path('sign/',views.sign),
    path('trans/',views.trans),
    path('saving/',saving),
    path('graph/',views.graph),
    path('calender/',views.calender),
    path('payment/',views.payment),
    path('savings/',views.savings),
    path('inserttrans/',views.inserttrans,name="inserttrans"),
]
