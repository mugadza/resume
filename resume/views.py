from django.shortcuts import render

def home(request):
    return render(request, 'resume/index.html')

def contact(request):
    return render(request, 'resume/contact.html')