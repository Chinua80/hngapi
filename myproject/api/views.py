# Create your views here.
from django.http import JsonResponse
import requests


def hello(request):
    visitor_name = request.GET.get('visitor_name', 'Guest')
    client_ip = request.META.get('REMOTE_ADDR')

    # Using ipinfo.io to get location data
    response = requests.get(f'https://ipinfo.io/{client_ip}/json')
    data = response.json()
    city = data.get('city', 'Unknown')

    # Hardcoding the temperature for demonstration
    temperature = 11  # In Celsius

    return JsonResponse({
        "client_ip": client_ip,
        "location": city,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"
    })
