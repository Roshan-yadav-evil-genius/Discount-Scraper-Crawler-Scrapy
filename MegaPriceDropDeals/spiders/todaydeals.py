import scrapy
from ..items import MegapricedropdealsItem
import pandas as pd


class TodaydealsSpider(scrapy.Spider):
    name = 'todaydeals'
    allowed_domains = ['www.pricebefore.com']
    # start_urls=
    def start_requests(self):
        for i in range(100):
            if i == 0:
                yield scrapy.Request(
                    url="https://www.pricebefore.com/price-drops/?price-drop=todaysDeals", callback=self.parse)
            else:
                yield scrapy.Request(url=f"https://www.pricebefore.com/price-drops/?price-drop=todaysDeals&page={i+1}&more=true", callback=self.parse)

    def parse(self, response):
        products = response.css("li.item .unit .body")

        for product in products:
            price_overview = product.css(
                "div.price-overview .item::text").getall()
            pages = product.css("div.btn-wrap a")
            platform = pages[1].css("::text").get().strip("Buy on")
            if platform == "Amaz":
                platform = "Amazon"
            item = MegapricedropdealsItem()
            item["title"] = product.css("div.title b a::text").get().strip()
            item["highest"] = price_overview[1].replace("\u20b9",""),
            item["lowest"] = product.css(
                "div.price-overview .item::text").get(),
            item["image"] = product.css("div.col-left a img::attr(data-src)").get(),
            item["platform"] = platform,
            item["history"] = pages[0].attrib['href'],
            item["page_link"] = pages[1].attrib['href'],
            item["mrp"] = product.css(
                "span.discount span.price-old::text").get()
            item["discount"] = product.css(
                "span.discount span.percent::text").get()
            if platform.lower() == "amazon":
                print(item["page_link"][0])
                yield scrapy.Request(response.urljoin(item["page_link"][0]), callback=self.parse_Amazonproductpage, cb_kwargs={"item": item})
            else:
                yield scrapy.Request(response.urljoin(item["page_link"][0]), callback=self.parse_Flipkartproductpage, cb_kwargs={"item": item})

            # print(item)
            # print(product.css("div.title b a::text").get().strip())

    def parse_Amazonproductpage(self, response, item):
        try:
            item["page_link"] = response.request.url
        except:
            pass
        try:
            item["allimage"] = response.css(
                "div#altImages li.item img::attr(src)").getall()
        except:
            pass
        try:
            table = response.css("div#productOverview_feature_div div table").get()
            item["details"] = {
                "specifications": pd.read_html(table)[0].set_index(0).to_dict()[1],
                "features": response.css("div#featurebullets_feature_div li span::text").getall()}
        except:
            pass
        yield item
        
    def parse_Flipkartproductpage(self, response, item):

        item["details"] = {
                "features": response.css("div._2418kt li::text").getall()}
        yield item
        
