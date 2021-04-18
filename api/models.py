from django.db import models


class Item(models.Model):
    description = models.CharField(max_length=200)
    in_use = models.BooleanField()
    replacement_link = models.CharField(max_length=200, null=True)
    replacement_cost = models.DecimalField(
        max_digits=19, decimal_places=2, null=True)
    category = models.ForeignKey(
        'Category', null=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(
        'Location', null=True, on_delete=models.SET_NULL)
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


class Location(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # TODO: Build in the ability for nested locations/sublocations
    # is_parent = models.BooleanField()
    # Relation for parent location, if it exists

    def __str__(self):
        return self.name
