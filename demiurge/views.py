from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'demiurge/index.html', {'lat': 42.65012181368025, 'lon': -3.9111328125})