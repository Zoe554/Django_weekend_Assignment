from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Quote(models.Model):
    quote_text = models.TextField()
    author = models.CharField(max_length=100)

    def __str__(self):
        return f'"{self.quote_text}" - {self.author}'


