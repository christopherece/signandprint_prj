from django.shortcuts import render, get_object_or_404
from .models import Service

# View for the services index page
def index(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})

# View for individual service details
def service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'services/service.html', {'service': service})

