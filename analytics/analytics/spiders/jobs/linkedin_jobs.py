import json
import scrapy


class LinkedinJobs(scrapy.Spider):

    name = "linkedin"
    collection_name = "jobs"

    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    }

    def start_requests(self):

        url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings'\
        '/search?location=Nairobi&trk=guest_homepage-basic_jobs-search-bar_search-submit&'\
        'redirect=false&position=1&pageNum=0&sortBy=DD'
        yield scrapy.Request(url=url, callback=self.parse_next_scroll_page)

    def parse_next_scroll_page(self, response):
        urls = [response.url]
        start_pages = [25, 50, 75, 100]
        for page in start_pages:
            next_page_url =  response.url + '&start={}'.format(page)
            urls.append(next_page_url)
       
        for url in urls:
            yield scrapy.Request(url=url, callback=self.get_jobs)

    def get_jobs(self, response):
        print(response.url)
        item = {}
        search_job_list = response.xpath("//li")
        for job in search_job_list:
            item['job_title'] = job.xpath(".//div[@class='result-card__contents job-result-card__contents']/h3/text()").extract()[0]
            path = job.xpath(".//div[@class='result-card__contents job-result-card__contents']/h4/a/text()").extract()
            if path:
                item['company'] = path[0]
            else:
                item['company'] = job.xpath(".//div[@class='result-card__contents job-result-card__contents']/h4/text()").extract()[0]
            item['location'] = job.xpath(".//div[@class='result-card__contents job-result-card__contents']//span/text()").extract()[0]
            item['time_posted'] = job.xpath(".//div[@class='result-card__contents job-result-card__contents']//time/text()").extract()[0]
            yield item
