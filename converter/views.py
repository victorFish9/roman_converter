from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .utils import roman_to_int

class RomanConverterView(View):
    def get(self, request):
        roman_numeral = request.GET.get('roman', '')
        result = None
        error = None

        if roman_numeral:
            try:
                result = roman_to_int(roman_numeral)
            except Exception as e:
                error = str(e)

        return render(request, 'converter/index.html', {'result': result, 'error': error})
