from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    # url(r'accounts/login/$', views.login, name='login'),
    # url(r'accounts/logout/$', views.logout,
    #     name='logout', kwargs={'next_page': '/'}),
]
