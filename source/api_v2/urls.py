from django.urls import path

from api_v2.views.articles import get_csrf_token
from api_v2.views.comments import CommentListView, CommentCreateView, CommentDetailView, CommentUpdateView, \
    CommentDeleteView
from source.api_v2.views import ArticleUpdateView, ArticleCreateView, ArticleDeleteView, \
    ArticleDetailView

app_name = 'api_v2'

urlpatterns = [
    path('get-token/', get_csrf_token, name='get_token'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('articles/<int:pk>/update/', ArticleUpdateView.as_view(), name='article'),
    path('articles/<int:pk>/add/', ArticleCreateView.as_view(), name='article'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article'),

    path('articles/<int:article_id>/comments/', CommentListView.as_view(), name='article'),
    path('articles/<int:article_id>/comments/add/', CommentCreateView.as_view(), name='article'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='article'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='article'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='article')
]
