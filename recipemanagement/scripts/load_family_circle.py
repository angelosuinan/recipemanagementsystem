#full path and name to your csv file
csv_filepathname="/home/suinan/projects/pyscrapy/pyscrapy/pyscrapy/x.csv"
import django
from products.models import Recipe
from products.models import Product
import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
dataReader

for row in dataReader:
    recipe = Recipe()
    if row[0] == 'direction':
        continue
    my_list = row[4].split(",")
    for pr in my_list:
        try:
            product = Product()
            product.name = pr
            price = 42.21
            product.save()
            recipe
            recipe = product
        except django.db.utils.IntegrityError:
            pass
    recipe.name = row[1]
    recipe.img_url = row[3]
    recipe.prep_time = row[8]
    recipe.servings = row[7]
    recipe.directions = row[0]
    recipe.ingredients = row[2]
    recipe.save()
