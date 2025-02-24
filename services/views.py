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


