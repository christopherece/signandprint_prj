from django.shortcuts import render
from services.models import Service  # Make sure to import the Service model

def index(request):
    services = Service.objects.all()  # Query all services
    return render(request, 'pages/index.html', {'services': services})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

