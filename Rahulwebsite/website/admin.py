from django.contrib import admin

# Register your models here.
from . models import Contact
from . models import Post, Category


admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(Category)
