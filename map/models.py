from django.db import models
from user.models import CustomUser


class Category(models.Model):
    category_name = models.TextField(blank=False)
    category_color = models.TextField(blank=False)

    def __str__(self):
        return str(self.pk) + " " + self.category_name
# Create your models here.
class Point(models.Model):
    latitude = models.DecimalField(max_digits=20,decimal_places=17)
    longtitude = models.DecimalField(max_digits=20,decimal_places=17)
    comment = models.TextField(blank=False)
    phone = models.TextField(blank=False)
    fullname = models.TextField(blank=False)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
