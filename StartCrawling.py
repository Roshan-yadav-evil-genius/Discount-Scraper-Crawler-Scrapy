from pprint import pprint
import time
import telegram
from telegram import MessageEntity
import json
from scrapy.settings import Settings
from scrapy.crawler import CrawlerProcess
from MegaPriceDropDeals.spiders.todaydeals import TodaydealsSpider
# with open('products.json',"w") as data:
#     pass
# settings = Settings()
# settings.set('FEED_URI', 'products.json')
# settings.set('FEED_FORMAT', 'json')
# process = CrawlerProcess(settings=settings)
# process.crawl(TodaydealsSpider)
# process.start()
print("Crawled")
with open('products.json') as data:
    allproducts = json.load(data)
properlist = []
for product in allproducts:
    for key, value in product.items():
        try:
            if len(value) == 1 and type(value) == list:
                product[key] = value[0]
        except:
            pass
        if key == "page_link":
            product[key] = value.rstrip(
                "?tag=toda07-21&linkCode=osi&th=1&psc=1")
    properlist.append(product)

with open("products.json", "w") as json_file:
    json_file.write(json.dumps(properlist))


token = "5751500197:AAG9EvfLStH2omedPilPtydaZ3IyQhbGRBY"
bot = telegram.Bot(token=token)
with open('products.json') as json_file:
    allproducts = json.load(json_file)
print(len(allproducts),"No of prroducts")
a=0
for product in allproducts:
    try:
        discount = int(product["discount"].strip("% Off"))
    except:
        continue
    if discount < 50:
        continue
    if not product["page_link"].startswith("https://"):
        continue

    caption = f"🗓 🎖 Today Drop to lowest From {product['mrp']} to {product['lowest']} 📉 \n\n {product['title']} \n\n Discount : {product['discount']} \n\n On 🗂 : {product['platform']} \n\n OnlyAt💸 : {product['lowest']} \n\n Link :{product['page_link']}\n\n"
    # try:
    #     specification = "Features\n"
    #     for key, value in product["details"]["specifications"].items():
    #         specification += f"{key} : {value}\n"
    #     specification += "\n\n"
    #     caption += specification
    # except:
    #     pass

    bot.send_photo(chat_id="-1001876326280",
                   caption_entities=[
                       MessageEntity(length=len(caption), offset=0, type="bold"), ],
                   photo=product['image'],
                   caption=caption)
    a+=1
    print(f"\rProduuct No : {a}",end="")
    time.sleep(10)
