from __future__ import unicode_literals
from django.db import models

class Cube(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=250)
    is_custom = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/product/%s/" % self.slug
