from rest_framework import serializers
from .models import TranslationRequest

class TranslationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationRequest
        fields = ('text', 'target_language', 'translated_text')
