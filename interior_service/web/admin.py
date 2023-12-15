from django.contrib import admin
from . models import Blog,Team,Testimonial,Category,Services

# Register your models here.
admin.site.register(Blog)
admin.site.register(Team)
admin.site.register(Testimonial)
admin.site.register(Category)
admin.site.register(Services)