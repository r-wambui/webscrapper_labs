import scrapy


class Myjobmag(scrapy.Spider):

    name = "tenders"

    def start_requests(self):
        
        url = [
            
        ]
        
        # work on the pagination
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_jobs)
    
    def get_jobs(self, response):
        pass

    

    