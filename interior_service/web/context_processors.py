from .models import Category

def service_categories(request):
    categories = Category.objects.all()
    return {'service_categories': categories}