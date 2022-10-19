
from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess
from MegaPriceDropDeals.spiders.todaydeals import TodaydealsSpider
import json
settings = Settings()
settings.set('FEED_URI', 'products.json')
settings.set('FEED_FORMAT', 'json')
process = CrawlerProcess(settings=settings)
process.crawl(TodaydealsSpider)
process.start()

print("Done")

with open('products.json') as json_file:
    allproducts = json.load(json_file)
properlist = []
for product in allproducts:
    for key, value in product.items():
        try:
            if len(value) == 1 and type(value) == list:
                print(key)
                product[key] = value[0]
        except:
            pass
        if key == "page_link":
            product[key] = value.rstrip(
                "?tag=toda07-21&linkCode=osi&th=1&psc=1")
    properlist.append(product)

with open("products.json", "w") as json_file:
    json_file.write(json.dumps(properlist, indent=2))
