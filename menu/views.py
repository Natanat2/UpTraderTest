from django.shortcuts import render


def home_view(request):
    return render(request, 'pages/home.html')


def about_view(request):
    return render(request, 'pages/about.html')


def contacts_view(request):
    return render(request, 'pages/contacts.html')


def services_view(request):
    return render(request, 'pages/services.html')


def web_services_view(request):
    return render(request, 'pages/web_services.html')


def mobile_services_view(request):
    return render(request, 'pages/mobile_services.html')
