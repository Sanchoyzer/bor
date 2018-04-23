from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='bor-index'),

    url(r'^quotes/$', views.QuotesAllListView.as_view(), name='quotes-all'),
    url(r'^quote/(?P<pk>\d+)$', views.QuoteDetailView.as_view(), name='quote-detail'),

    url(r'^quote/(?P<pk>\d+)/rulez/$', views.quote_rulez, name='quote-rulez'),
    url(r'^quote/(?P<pk>\d+)/sux/$', views.quote_sux, name='quote-sux'),
    url(r'^quote/(?P<pk>\d+)/bayan/$', views.quote_bayan, name='quote-bayan'),

    url(r'^comment/(?P<pk>\d+)$', views.CommentDetailView.as_view(), name='comment-detail'),
]
