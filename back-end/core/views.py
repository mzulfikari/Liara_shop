from django.shortcuts import render,redirect
from .forms import ContactUsForm
from Products.models import Products
from django.db import models

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:home')
    else:
        form = ContactUsForm()

    context = {
        'form': form
    }
    return render(request, 'core/contact.html', context)


def about(request):
    return render(request, 'core/about.html')