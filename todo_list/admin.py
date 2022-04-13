from django.contrib import admin

# Register your models here.
from .models import User, Todo, Categories, Events

admin.site.register(User)
admin.site.register(Todo)
admin.site.register(Categories)
admin.site.register(Events)