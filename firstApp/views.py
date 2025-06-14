from django.shortcuts import render, HttpResponse
# Create your views here.

def firstPage(request):
    return  render(request, 'index.html')

def About(request):
    return render(request, 'About.html')

def Catalog(request):
    return render(request, 'Catalog.html')

def ItemPage(request):
    return render(request, 'includes/templates/ItemPage.html')