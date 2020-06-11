from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    path('resources/', views.resources, name='resources'),
    path('like/', views.like, name='post_like'),
    path('properties/', views.PropertyList.as_view(), name='property_list'),
    path('property/<slug:slug>/', views.PropertyDetail.as_view(), name='property_detail'),
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
