from django.shortcuts import render, get_object_or_404
from .models import Service, Item

# View for the services index page
def index(request):
    services = Service.objects.all()
    items = Item.objects.all()
    context = {
        'services': services,
        'items': items,
    }
    return render(request, 'services/services.html', context)

# View for individual service details
def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'services/item_detail.html', {'item': item})

def service_view(request, service_id):
    service = Service.objects.filter(id=service_id).first()
    items = Item.objects.filter(service=service)
    context = {
        'service': service,
        'items': items,
    }
    return render(request, 'services/signage.html', context)