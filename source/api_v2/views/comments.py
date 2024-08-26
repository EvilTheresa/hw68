from django.http import HttpResponse, HttpResponseNotAllowed

from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.comment import CommentSerializer
from webapp.models.comment import Comment


class CommentListView(APIView):
    def get(self, request, article_id):
        comments = Comment.objects.filter(article_id=article_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentDetailView(APIView):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentCreateView(APIView):
    def post(self, request, article_id):
        data = request.data.copy()
        data['article'] = article_id
        serializer = CommentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        comment_data = CommentSerializer(comment).data
        return Response(comment_data, status=status.HTTP_201_CREATED)


class CommentUpdateView(APIView):
    def put(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        comment_data = CommentSerializer(comment).data
        return Response(comment_data, status=status.HTTP_201_CREATED)


class CommentDeleteView(APIView):
    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
