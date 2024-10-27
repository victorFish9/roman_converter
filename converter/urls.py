from django.urls import path
from .views import RomanConverterView

urlpatterns = [
    path('convert/', RomanConverterView.as_view(), name='roman_convert'),
]
