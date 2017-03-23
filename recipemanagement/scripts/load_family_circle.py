#full path and name to your csv file
import os
__location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = __location__+"/a.csv"
from products.models import Recipe
from products.models import Product
import django
import csv
dataReader = csv.reader(open(f), delimiter=',', quotechar='"')
import random
for row in dataReader:
   try:
        if row[0] == 'direction':
	    print ("SDFDFAS")
	    continue
	recipe = Recipe()
	recipe.name = row[1]
	recipe.img_url = row[8]
	recipe.prep_time = row[6]
	recipe.servings = row[7]
	recipe.direction = row[0]
	recipe.ingredients = row[2]
	my_list = row[4].split(",")
	recipe.save()
	for pr in my_list:
	    try:
	        product = Product()
                product.name = pr
                product.price =  round(random.uniform(10.00,500),2)
                product.save()
                p = Product.objects.get(name=product.name)
                recipe.products.add(p)
            except django.db.utils.IntegrityError:
                old = Product.objects.get(name=pr)
                recipe.products.add(old)
        recipe.save()
   except  django.db.utils.IntegrityError:
        continue
