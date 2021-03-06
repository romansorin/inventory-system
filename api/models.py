from django.db import models


class Item(models.Model):
    description = models.CharField(max_length=200)
    in_use = models.BooleanField()
    replacement_link = models.URLField(
        max_length=200, blank=True, null=True)
    replacement_cost = models.DecimalField(
        max_digits=19, blank=True, decimal_places=2, null=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(
        'Location', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # TODO: Build in the ability for nested locations/sublocations
    # is_parent = models.BooleanField()
    # Relation for parent location, if it exists

    def __str__(self):
        return self.name
