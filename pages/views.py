from django.shortcuts import render
from services.models import Service, Item  # Make sure to import the Service model

def index(request):
    services = Service.objects.all()
    items = Item.objects.all()
    context = {
        'services': services,
        'items': items,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')

