from rest_framework import serializers

from webapp.models.article import Article


class ArticleSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        return super().validate(attrs)

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Длина должна быть больше пяти")
        return value
    class Meta:
        model = Article
        fields = ['id', 'title', 'content',  "status", "tags", "created_at", "updated_at", "author"]
        read_only_fields = ['id', 'created_at', 'updated_at', 'author']