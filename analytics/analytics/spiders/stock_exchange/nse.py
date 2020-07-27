import scrapy
import json

class NairobiStockExchange(scrapy.Spider):

    name = "nse"
    collection_name = "stock_exchange"

    def start_requests(self):
        url = 'https://deveintapps.com/nseticker/api/v1/ticker'
        yield scrapy.Request(url=url, method="POST", callback=self.get_pages)

    def get_pages(self, response):
        response_data = json.loads(response.body)
        last_page = response_data['message'][0]['snapshot']['last_page']

        for page in range(1, int(last_page)+1, ):
            url = response.url + "?page=" + str(page)
            yield scrapy.Request(url=url, method="POST", callback=self.get_stock_prices)
 
    def get_stock_prices(self, response):
        item = {}
        response_data = json.loads(response.body)['message'][0]['snapshot']['data']
        date = json.loads(response.body)['message'][1]['updated_at']['date']
        time = json.loads(response.body)['message'][1]['updated_at']["time"]
        datetime_created =  date + " " + time

        for row in response_data:
            item["datetime_created"] = datetime_created
            item["company"] = row["issuer"]
            item['price'] = row["price"]
            item["ltp"] = row["ltp"]
            item["prev_price"] = row["prev_price"]
            item["today_open"] = row["today_open"]
            item["today_high"] = row["today_high"]
            item["today_low"] = row["today_low"]
            item["turnover"] = row["turnover"]
            item["volume"] = row["volume"]
            item["change"] = row["change"]
            item["today_close"] = row["today_close"]
            yield item
