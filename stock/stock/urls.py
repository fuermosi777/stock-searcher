from django.conf.urls import include, url
from django.contrib import admin
from stocksearch.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'stock.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home),
    url(r'^result/', result),
]
