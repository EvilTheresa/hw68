from django.urls import path

from api_v2.views.articles import get_csrf_token
from source.api_v2.views import ArticleUpdateView, ArticleCreateView, ArticleDeleteView, \
    ArticleDetailView

app_name = 'api_v2'

urlpatterns = [
    path('get-token/', get_csrf_token, name='get_token'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('articles/<int:pk>/update/', ArticleUpdateView.as_view(), name='article'),
    path('articles/<int:pk>/add/', ArticleCreateView.as_view(), name='article'),
    path('articles/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article'),
]
