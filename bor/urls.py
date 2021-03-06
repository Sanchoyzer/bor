from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='bor-index'),

    url(r'^quotes/$',   views.QuotesAllListView.as_view(),      name='quotes-all'),
    url(r'^hidebad/$',  views.QuotesHideBadListView.as_view(),  name='quotes-hide-bad'),
    url(r'^random/$',   views.QuotesRandomListView.as_view(),   name='quotes-random'),
    url(r'^new/$',      views.QuotesNewListView.as_view(),      name='quotes-new'),
    url(r'^byrating/$', views.QuotesByRatingListView.as_view(), name='quotes-by-rating'),
    url(r'^abyss/$',    views.QuotesAbyssListView.as_view(),    name='quotes-abyss'),
    url(r'^abysstop/$', views.QuotesAbyssTopListView.as_view(), name='quotes-abysstop'),

    url(r'^quote/(?P<pk>\d+)$',        views.QuoteDetailView.as_view(),      name='quote-detail'),
    url(r'^quote/(?P<pk>\d+)/rulez/$', views.quote_rulez,                    name='quote-rulez'),
    url(r'^quote/(?P<pk>\d+)/sux/$',   views.quote_sux,                      name='quote-sux'),
    url(r'^quote/(?P<pk>\d+)/bayan/$', views.quote_bayan,                    name='quote-bayan'),
    url(r'^quote/search$',             views.QuotesSearchListView.as_view(), name='quote-search'),

    url(r'^comment/(?P<pk>\d+)$', views.CommentDetailView.as_view(), name='comment-detail'),
]
