'''
Created on Jul 6, 2019

@author: sjpat
'''
from django.conf.urls import url
from . import views 
from .views import ListPostView
from django.urls import path
from .models import Post,Comment
from .serializers import PostSerializer
from rest_framework import generics

urlpatterns = [
        url(r'post/(?P<pk>\d+)$',views.PostDetailView.as_view(), name='post_detail'),
        url(r'^$',views.PostListView.as_view(),name='post_list'),       
        url(r'^about/$',views.AboutView.as_view(),name='about'),
        url(r'^post/new/$', views.CreatePostView.as_view(),name='post_new'),
        url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(),name='post_edit'),
        url(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_remove'),
        url(r'^drafts/$', views.DraftListView.as_view(),name='post_draft_list'),
        url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
        url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve, name='comment_approve'),
        url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove, name='comment_remove'),
        url(r'^post/(?P<pk>\d+)/publish/$',views.post_publish, name='post_publish'),
        path('posts/',ListPostView.as_view(queryset=Post.objects.all(), serializer_class=PostSerializer), name='post_api_view'),
               
    ]
