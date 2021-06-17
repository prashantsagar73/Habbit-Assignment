from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# Category of Product


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Product Model


class Product(models.Model):

    class ProductObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)
    # Protect will not affect the product if you delete the Category
    course = models.CharField(max_length=550)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses')
    published = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=250, unique_for_date='published')

    # Cascade is if you delete any user it will also delete the products
    status = models.CharField(
        max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manger
    productobjects = ProductObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.course
