from django.shortcuts import render, redirect
from services.models import Service, Item  # Make sure to import the Service model
from .forms import ContactForm
from django.contrib import messages



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

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Contact

def contact(request):
    if request.method == 'POST':
        # Get the submitted data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        category = request.POST.get('category')
        description = request.POST.get('description')

        # Create a Contact object and save it to the database
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            category=category,
            description=description
        )
        contact.save()

        # Show a success message after submission
        messages.success(request, "Your message has been sent successfully.")
    else:
        # If not a POST request, just render the page
        pass

    # Render the contact page with the form
    return render(request, 'pages/index.html')
