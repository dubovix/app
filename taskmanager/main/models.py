from django.db import models

class Task(models.Model):
    title = models.CharField("Name", max_length=50)
    task = models.TextField("Comment")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
