"""django_project URL Configuration
/*************************************************************
*   Author          : H M Fazle Rabbi
*   Date Modified   : 20190919_2040
 *   Description    : Url file created
*************************************************************/
"""
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), #pk is what it expects it to be
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'), #pk is what it expects it to be
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'), #pk is what it expects it to be
    path('post/new/', PostCreateView.as_view(), name='post-create'), #pk is what it expects it to be
    path('about/', views.about, name='blog-about'),
]
