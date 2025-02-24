from django.shortcuts import render, redirect
from django.contrib import messages  # <-- Import this
from .models import Contact

def inquiry(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        item = request.POST['item']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        # user_id = request.POST['user_id']

        contact = Contact(item=item, item_id=item_id, name=name, email=email, phone=phone, message=message)
        contact.save()
        
        messages.success(request, 'Your request has been submitted and we will get back to you soon')  # <-- Fixed 'messages'
        return redirect(f'/services/item/{item_id}')
    else:
        messages.error(request, 'There was an error with your request. Please try again.')  # <-- Better error message
        return redirect(f'/services/item/{item_id}')
