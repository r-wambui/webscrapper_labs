import scrapy


class BrighterMonday(scrapy.Spider):
    name = "jobs"

    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    }

    def start_requests(self):
        urls =[
            'https://www.brightermonday.co.ke/jobs/software-data',
            'https://www.brightermonday.co.ke/jobs/engineering-technology'

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_pages)

    def parse_pages(self, response): 
        url = response.url
        page_urls = [url]
        total_pages = int(response.xpath("//li[@class='page-item'][position()=\
                                        last()-1]/a/text()").extract_first())
        for page in range(2, total_pages + 1):
            page_url = url + "?page=" + str(page)
            page_urls.append(page_url)
        for url in page_urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
    def parse(self, response):

        Job_listing = response.xpath("//div[@class='search-main__content']")
        Job_titles = Job_listing.xpath("//header[@class='search-result__header']\
                                            //h3/text()").getall()
        Company = Job_listing.xpath("//header[@class='search-result__header']\
                                    //a[contains(@href, '/jobs?')]/text()").getall()
        Location = Job_listing.xpath("//header[@class='search-result__header']\
                                    //div[@class='search-result__location']/text()").getall()
        Date_posted = Job_listing.xpath("//header[@class='search-result__header']\
                                        //div[@class='if-wrapper-column align-self--end text--right']/text()").getall()
           

        
    