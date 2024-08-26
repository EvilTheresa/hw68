from django.http import HttpResponse, HttpResponseNotAllowed

from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import ArticleSerializer
from webapp.models.article import Article


# Create your views here.
@ensure_csrf_cookie
def get_csrf_token(request):
    if request.method == 'GET':
        return HttpResponse()
    else:
        return HttpResponseNotAllowed(permitted_methods=["GET"])

class ArticleDetailView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.order_by('-created_at')
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleCreateView(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data.copy()
        serializer = ArticleSerializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        article_data = ArticleSerializer(article).data
        return Response(article_data, status=status.HTTP_201_CREATED)


class ArticleUpdateView(APIView):
    def put(self, request, *args, pk, **kwargs):
        article = get_object_or_404(Article, pk=pk)
        serializer = ArticleSerializer(data=request.data, instance=article)
        serializer.is_valid(raise_exception=True)
        article = serializer.save()
        article_data = ArticleSerializer(article).data
        return Response(article_data, status=status.HTTP_200_OK)


class ArticleDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)