from django.shortcuts import render, redirect
from .models import Item
from redis import Redis


redis = Redis(host='redis', port=6379)

def home(request):
    context = {
        'heading': 'clean blog',
        'subheading': 'A Clean Blog Theme by Start Bootstrap',
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'heading': 'About me',
        'subheading': 'A Clean Blog Theme by Start Bootstrap',
    }
    return render(request, 'about.html', {})

def contact(request):
    context = {
        'heading': 'Contact me',
        'subheading': 'A Clean Blog Theme by Start Bootstrap',
    }
    return render(request, 'contact.html', {})
