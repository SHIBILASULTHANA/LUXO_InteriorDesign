from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('services',views.services,name='services'),
    path('categories/<int:category_id>/', views.service_details, name='service_details'),
    path('gallery',views.gallery,name='gallery'),
    path('blog',views.blog,name='blog'),
    path('<int:blog_id>/', views.blog_details, name='blog_details'),
    path('error',views.error,name='error'),
    path('contactus',views.contactus,name='contactus')
]