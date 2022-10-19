from telegram import MessageEntity
import telegram
import json
import time
token = "5751500197:AAG9EvfLStH2omedPilPtydaZ3IyQhbGRBY"
bot = telegram.Bot(token=token)
with open('417data.json') as json_file:
    allproducts = json.load(json_file)

for product in allproducts:
    discount = int(product["discount"].strip("% Off"))
    if discount<50:
        continue
    caption = f"🗓 🎖 Today Drop to lowest From {product['mrp']} to ₹{product['lowest']} 📉 \n\n {product['title']} \n\n Discount : {product['discount']} \n\n On 🗂 : {product['platform']} \n\n OnlyAt💸 : ₹{product['lowest']} \n\n Link :{product['page_link']}\n\n"
    try:
        specification = "Features\n"
        for key,value in product["details"]["specifications"].items():
            specification+=f"{key} : {value}\n"
        specification+="\n\n"
        caption+=specification
    except:
        pass


    bot.send_photo(chat_id="-1001876326280",
                   caption_entities=[
                       MessageEntity(length=len(caption), offset=0, type="bold"), ],
                   photo=product['image'],
                   caption=caption)
    time.sleep(10)
