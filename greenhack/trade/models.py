from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	name = models.TextField(null=True)
	brand = models.TextField(null=True)
	strain = models.TextField(null=True)
	ctype = models.TextField(null=True)
	thc = models.DecimalField(max_digits=8, decimal_places=2, null=True)
	cbd = models.DecimalField(max_digits=8, decimal_places=2, null=True)


class Posting(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	description = models.TextField()
	title = models.CharField(max_length=200)
	wishlist = models.TextField(null=True)
	price = models.DecimalField(max_digits=12, decimal_places=2, null=True)
	quantity = models.DecimalField(max_digits=10, decimal_places=4)
	image = models.ImageField(upload_to='images/', null=True)
	date_time = models.DateTimeField(auto_now_add=True)
	lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
	lon = models.DecimalField(max_digits=9, decimal_places=6, null=True)
