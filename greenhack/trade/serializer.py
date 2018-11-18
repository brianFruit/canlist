from django.core import serializers
from trade.models import Product, Posting

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 
        		  'brand', 
        		  'strain', 
        		  'ctype', 
        		  'thc', 
        		  'cbd')

class PostingSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()

    class Meta:
        model = Posting
        fields = ('title',
        		  'description',
        		  'wishlist',
        		  'quantity',
        		  'date_time')
