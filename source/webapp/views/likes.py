from django.http import JsonResponse
from django.views import View
from ..models import ArticleLike, CommentLike, Article, Comment
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class ArticleLikeToggle(View):
    def post(self, request, article_id):
        article = Article.objects.get(id=article_id)
        like, created = ArticleLike.objects.get_or_create(user=request.user, article=article)

        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        return JsonResponse({'likes_count': article.count_likes(), 'liked': liked})


class CommentLikeToggle(View):
    def get(self, request, comment_id):
        comment = Comment.objects.get(id=comment_id)
        like, created = CommentLike.objects.get_or_create(user=request.user, comment=comment)

        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        return JsonResponse({'likes_count': comment.count_likes(), 'liked': liked})
