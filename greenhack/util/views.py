from django.shortcuts import render
from django.http import HttpResponse
from trade.models import Product

import requests
import json

# Create your views here.
def is_number(s):
	try:
		float(s)
		return True
	except (ValueError, TypeError) as e:
		return False


def upload_products(request):
	resp = requests.get('https://api.calivahack.io/products/v2/retail', headers = {'apikey':'Caliva420'})
	resp_dict = json.loads(resp.text)
	if resp_dict['status'] == 200 and resp_dict['message'] == 'ok':
		all_products = resp_dict['data']['all']
		for uuid in all_products:
			print (all_products[uuid]['tests']['thc'], all_products[uuid]['tests']['cbd'])
			thc = all_products[uuid]['tests']['thc'] if is_number(all_products[uuid]['tests']['thc']) else None
			cbd = all_products[uuid]['tests']['cbd'] if is_number(all_products[uuid]['tests']['cbd']) else None
			Product.objects.create(name=all_products[uuid]['name'], 
								   brand=all_products[uuid]['brand'],
								   strain=all_products[uuid]['species'],
								   ctype=all_products[uuid]['type'],
								   thc=thc,
								   cbd=cbd)
		return HttpResponse(200)
	return HttpResponse(resp_dict['status'])