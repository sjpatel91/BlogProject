"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
#from django.conf.urls import urls,include
from django.urls import path,include, re_path
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    # url(r'accounts/login/$',views.login, name= 'login'),
    path('accounts/login', auth_views.LoginView.as_view(), name='login'),
    #url(r'accounts/logout/$',views.logout,name='logout',kwargs={'next_page':'/'})
    path('accounts/logout',auth_views.LogoutView.as_view(), name='logout',kwargs={'next_page':'/'}),
    re_path('api/(?P<version>(v1|v2))/', include('blog.urls')),
]
