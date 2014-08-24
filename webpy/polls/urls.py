from django.conf.urls import patterns, include, url
from polls import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webpy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),

)
