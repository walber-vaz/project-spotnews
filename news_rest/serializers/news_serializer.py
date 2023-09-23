from rest_framework import serializers

from news.models import Categories, News


class NewsSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Categories.objects.all(), allow_empty=False
    )

    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "content",
            "author",
            "created_at",
            "image",
            "categories",
        ]
