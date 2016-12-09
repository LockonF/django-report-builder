from rest_framework import serializers

class CustomTitlesSerializer(serializers.Serializer):
    titles = serializers.ListField()

class ReportPreviewSerializer(serializers.Serializer):
    meta = CustomTitlesSerializer(read_only=True)
    data = serializers.ListField()