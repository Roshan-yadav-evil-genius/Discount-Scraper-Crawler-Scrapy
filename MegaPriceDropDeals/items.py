# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MegapricedropdealsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    image=scrapy.Field()
    allimage=scrapy.Field()
    highest=scrapy.Field()
    lowest=scrapy.Field()
    platform=scrapy.Field()
    history=scrapy.Field()
    page_link=scrapy.Field()
    mrp=scrapy.Field()
    discount=scrapy.Field()
    details=scrapy.Field()
