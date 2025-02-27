from django.shortcuts import render, redirect
from django.contrib import messages  # <-- Import this
from .models import Contact

def inquiry(request):
    if request.method == 'POST':
        item = request.POST.get('item')
        item_id = request.POST.get('item_id')  # <-- Safe access
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact = Contact(item=item, item_id=item_id, name=name, email=email, phone=phone, message=message)
        contact.save()
        
        messages.success(request, 'Your request has been submitted and we will get back to you soon')  # <-- Fixed 'messages'
        return redirect(f'/services/item/{item_id}')
    else:
        messages.error(request, 'There was an error with your request. Please try again.')  # <-- Better error message
        return redirect(f'/services/item/{item_id}')
