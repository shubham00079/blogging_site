from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'^about/$',views.About.as_view(),name='about'),
    url(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'^post/create/$',views.PostCreateView.as_view(),name='post_create'),
    url(r'^post/(?P<pk>\d+)/update/$',views.PostUpdateView.as_view(),name='post_update'),
    url(r'^post/(?P<pk>\d+)/delete/$',views.PostDeleteView.as_view(),name='post_delete'),
    url(r'^post/draft/$',views.PostDraftView.as_view(),name='draft'),
    url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish,name='post_publish'),
]
