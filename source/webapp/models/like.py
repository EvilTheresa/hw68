from django.contrib.auth import get_user_model
from django.db import models


class ArticleLike(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        related_name="article_likes",
        on_delete=models.SET_DEFAULT,
        default=1
    )
    article = models.ForeignKey('webapp.Article', on_delete=models.CASCADE)


class CommentLike(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        related_name="comments_likes",
        on_delete=models.SET_DEFAULT,
        default=1
    )
    comment = models.ForeignKey('webapp.Comment', on_delete=models.CASCADE)
