from django.contrib import admin
from . models import About, Services, Blog, Contact, Clientels, Testimonials, Gallery, Socials




class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'time']
    ordering = ['text']



admin.site.register(About)
admin.site.register(Services)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
admin.site.register(Clientels)
admin.site.register(Testimonials)
admin.site.register(Gallery)
admin.site.register(Socials)