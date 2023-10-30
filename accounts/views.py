from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import TranslationRequest
from .serializers import TranslationRequestSerializer
from translate import Translator

class TranslationRequestView(generics.CreateAPIView):
    queryset = TranslationRequest.objects.all()
    serializer_class = TranslationRequestSerializer

    def post(self, request):
        serializer = TranslationRequestSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            target_language = serializer.validated_data['target_language']

            translator = Translator(to_lang=target_language)
            translated_text = translator.translate(text)

            return Response({"data":translated_text}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': "target_language is invalid"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)