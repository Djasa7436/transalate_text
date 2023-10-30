# translation_app/urls.py
from django.urls import path
from .views import TranslationRequestView

urlpatterns = [
    path('translations/', TranslationRequestView.as_view(), name='translation-list'),
]
 