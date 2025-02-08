from django.db import models

# Create your models here.
class Editorial(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name
    # pass

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name="book")
    synopsis = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    # pass