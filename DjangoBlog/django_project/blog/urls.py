"""django_project URL Configuration
/*************************************************************
*   Author          : H M Fazle Rabbi
*   Date Modified   : 20190919_2040
 *   Description    : Url file created
*************************************************************/
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
