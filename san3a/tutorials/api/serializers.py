from rest_framework import serializers

from ..models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Tutorial
        fields = [
            "id",
            "title",
            "author",
            "description",
            "video",
            "created",
            "modified",
        ]


class TutorialSerializerWriter(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = [
            "id",
            "title",
            "author",
            "description",
            "video",
            "created",
            "modified",
        ]
