import scrapy


class Myjobmag(scrapy.Spider):

    name = "treasury_tenders"

    def start_requests(self):
        
        url = [
            'https://www.myjobmag.co.ke/jobs-by-field/engineering',
            'https://www.myjobmag.co.ke/jobs-by-field/information-technology'
        ]
        
        # work on the pagination
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_jobs)
    
    def get_jobs(self, response):
        pass

    

    