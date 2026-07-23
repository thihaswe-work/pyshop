from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:category", kwargs={"slug": self.slug})


class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True)
    price = models.FloatField()
    stock = models.IntegerField()
    imageUrl = models.CharField(max_length=1208, blank=True)
    image = models.ImageField(upload_to="products/", blank=True, null=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="products"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={"slug": self.slug})


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    discount = models.FloatField()

    def __str__(self):
        return self.code
