import scrapy


class BrighterMonday(scrapy.Spider):
    name = "jobs"

    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    }

    def start_requests(self):
        urls = [
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
        item = {}
        Job_listing = response.xpath("//div[@class='search-main__content']/*\
                                /header[@class='search-result__header']")
        for job in Job_listing:
            item['job_title'] = job.xpath(".//h3/text()").extract()[0]
            item["company"] = job.xpath(".//a[contains(@href, '/jobs?')]/text()").extract()
            item['location'] = job.xpath(".//div[@class='search-result__location']/text()").extract()[0]
            item["time_posted"] = job.xpath("//div[@class='if-wrapper-column align-self--end text--right']/text()").extract()[0]
            yield item
        yield item
