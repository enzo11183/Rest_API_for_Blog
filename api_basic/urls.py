from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api_basic import views

from django.views.generic import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url='/posts'), name = 'yonlendir'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name = 'comment-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)