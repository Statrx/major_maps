from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import Pothole
from .serializers import PotholeSerializer


def map_view(request):
    context = {
        'GOOGLE_API_KEY': settings.GOOGLE_API_KEY,
    }
    return render(request, 'map_view.html', context)

def get_potholes(request):
    potholes = Pothole.objects.all()
    serializer = PotholeSerializer(potholes, many=True)
    return JsonResponse(serializer.data, safe=False)
