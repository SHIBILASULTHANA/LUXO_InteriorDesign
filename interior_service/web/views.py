from django.shortcuts import render,get_object_or_404
from .models import  Blog,Team,Testimonial,Category,Services

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    testimonial = Testimonial.objects.all()
    services = Services.objects.all()
    context = {
        'blogs': blogs,
        'testimonial': testimonial,
        'services' : services
    }
    return render(request,'web/home.html',context)

def aboutus(request):
    team = Team.objects.all()
    testimonial = Testimonial.objects.all()
    context = {
        'team': team,
        'testimonial': testimonial
    }
    return render(request,'web/aboutus.html',context)

def services(request):
    return render(request,'web/services.html')

def service_details(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'web/service_details.html', {'category': category})

def gallery(request):
    services = Services.objects.all()
    context = {
        'services' : services
    }
    return render(request,'web/gallery.html',context)

def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'web/blog.html', context)

def blog_details(request, blog_id):
    blogs = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'web/blog_details.html', {'blog': blogs})

def error(request):
    return render(request,'web/error.html')

def contactus(request):
    return render(request,'web/contactus.html')