from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
# from blog import views
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    # url(r'accounts/login/$', views.login, name='login'),
    # url(r'accounts/logout/$', views.logout,
    #     name='logout', kwargs={'next_page': '/'}),
]

# handler404 = 'blog.views.handler404'
# handler500 = 'blog.views.handler500'

handler404 = 'blog.views.notfound'
