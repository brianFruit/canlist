from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from trade.models import Product, Posting
from django.contrib.auth.models import User
from django.core import serializers

import json

# Create your views here.
def index(request):
	return HttpResponse("HERE")

@csrf_exempt
def post(request):
	# try:
	data = json.loads(request.body)
	print (data)
	if "product_id" in data:
		product_id = data["product_id"]
		product = Product.objects.filter(id=product_id)[0]
	else:
		name = data['name']
		brand = data['brand']
		strain = data['strain']
		ctype = data['ctype']
		thc = float(data['thc'])
		cbd = float(data['cbd'])
		product = Product.objects.create(name=name, brand=brand, strain=strain, ctype=ctype, thc=thc, cbd=cbd)
	user = User.objects.filter(username='anonymous')[0]
	title = data['title']
	description = data['description']
	wishlist = data['wishlist']
	quantity = data['quantity']
	post = Posting.objects.create(product=product, user=user, description=description, quantity=quantity, wishlist=wishlist, title=title)
	return HttpResponse("SUCCESS")
	# except e:
	# 	return HttpResponse("FAIL")


@csrf_exempt
def listing(request):
	data = json.loads(request.body)
	print(data)
	strain = data['strain']
	posting = Posting.objects.filter(product__strain=strain)
	json_posts = serializers.serialize('json', posting, use_natural_primary_keys=True, use_natural_foreign_keys=True)
	print (json_posts)

	l = []
	for row in posting:
		product = Product.objects.filter(id=row.product_id)[0]
		l.append({"name":product.name, 
				  "brand":product.brand, 
				  "strain":product.strain, 
				  "ctype":product.ctype,
				  "thc":str(product.thc),
				  "cbd":str(product.cbd),
				  "title":row.title,
				  "description":row.description,
				  "wishlist":row.wishlist,
				  "quantity":str(row.quantity),})
	return HttpResponse(json.dumps(l), content_type='application/json')

