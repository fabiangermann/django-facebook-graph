from django.conf.urls.defaults import patterns, url

from views import redirect_to_slug

urlpatterns = patterns('',
    url(r'^$', redirect_to_slug, name='redirect_to_slug'),
)
