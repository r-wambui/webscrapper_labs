import scrapy


class Myjobmag(scrapy.Spider):

    name = "myjobmag"

    def start_requests(self): 
        urls = [
            'https://www.myjobmag.co.ke/jobs-by-field/engineering',
            'https://www.myjobmag.co.ke/jobs-by-field/information-technology'
        ]    
        # work on the pagination
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_jobs)

    def get_jobs(self, response):
        item = {}
        search_job_list = response.xpath("//ul[@class='job-list']/li")
        for job in search_job_list:
            job_title = job.xpath(".//li[@class='job-info']//li[@class='mag-b']/h2/a/text()").extract()
            if job_title:
                item["job_title"] = job_title[0]
            company = None  # text analysis from the title
            loaction = job.xpath(".//li[@class='job-info']//li[@class='job-desc']/text()").extract()


            print(loaction)
      
# time out 