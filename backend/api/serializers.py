from rest_framework import serializers

class PdfUploadSerializer(serializers.Serializer):
    file = serializers.FileField()