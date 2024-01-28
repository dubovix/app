
from django.db import models

from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField("Name", max_length=50)
    task = models.TextField("Comment")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class ContactForm(models.Model):
    name = models.CharField("Name", max_length=50)
    email = models.TextField("email")
    message = models.TextField("message")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Contact form"
        verbose_name_plural = "Contact form"
