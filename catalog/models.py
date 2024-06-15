from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published_date = models.DateTimeField(auto_now_add=True, editable=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='books', null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

