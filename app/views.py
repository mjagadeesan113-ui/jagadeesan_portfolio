from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def experience(request):
    return render(request, 'experience.html')

def contact(request):
    return render(request, 'contact.html')