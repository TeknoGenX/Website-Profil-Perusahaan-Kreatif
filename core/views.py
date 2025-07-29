from django.shortcuts import render
from .models import *

def home(request):
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()[:3]
    testimonials = Testimonial.objects.all()
    info = CompanyInfo.objects.first()
    return render(request, 'core/home.html', {
        'services': services,
        'portfolios': portfolios,
        'testimonials': testimonials,
        'info': info
    })

def about(request):
    info = CompanyInfo.objects.first()
    return render(request, 'core/about.html', {'info': info})

def services(request):
    return render(request, 'core/services.html', {'services': Service.objects.all()})

def portfolio(request):
    return render(request, 'core/portfolio.html', {'portfolios': Portfolio.objects.all()})

def team(request):
    return render(request, 'core/team.html', {'team': TeamMember.objects.all()})

def contact(request):
    info = CompanyInfo.objects.first()
    return render(request, 'core/contact.html', {'info': info})
