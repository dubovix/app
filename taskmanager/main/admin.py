from django.contrib import admin

from .models import Task, ContactForm

admin.site.register(Task)
admin.site.register(ContactForm)