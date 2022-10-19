import json
with open('products.json') as json_file:
    allproducts = json.load(json_file)
properlist = []
for product in allproducts:
    for key, value in product.items():
        try:
            if len(value) == 1 and type(value) == list:
                product[key] = value[0]
        except:
            pass
        if key == "page_link":
            try:
                product[key] = value.rstrip(
                    "?tag=toda07-21&linkCode=osi&th=1&psc=1")
            except:
                try:
                    product[key] = value[0].rstrip(
                        "?tag=toda07-21&linkCode=osi&th=1&psc=1")
                except:
                    print("Error pagelink")
            
    properlist.append(product)

with open("products.json", "w") as json_file:
    json_file.write(json.dumps(properlist, indent=2))
