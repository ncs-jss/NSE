from django.conf.urls import include, url
from django.contrib import admin
import nsestock,login
urlpatterns = [
    # Examples:
    # url(r'^$', 'nse.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^nse/',include('nsestock.urls')),
    url(r'^account/',include('login.urls')),
    url(r'',nsestock.views.base.as_view()),
]
