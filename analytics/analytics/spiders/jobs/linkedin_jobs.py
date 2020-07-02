import scrapy


class LinkedinJobs(scrapy.Spider):

    name = "linkedin"
    collection_name = "jobs"

    def start_requests(self):
        url = 'https://www.linkedin.com/jobs/search?location=Nairobi%2C%'\
            '2BNairobi%2C%2BKenya&trk=homepage-jobseeker_jobs-search-bar_search-'\
            'submit&sortBy=DD&redirect=false&position=1&pageNum=0'\

        yield scrapy.Request(url=url, callback=self.get_jobs)

    def get_jobs(self, response):
        item = {}
        search_job_list = response.xpath("//ul[@class='jobs-search__results-list']/li")
        for job in search_job_list:
            item['job_title'] = job.xpath(".//div[@class='result-card__contents job-result-card__contents']/h3/text()").extract()[0]
            item['company'] = job.xpath(".//div[@class='result-card__contents job-result-card__contents']/h4/a/text()").extract()
            item['location'] = job.xpath(".//div[@class='result-card__contents job-result-card__contents']//span/text()").extract()[0]
            item['time_posted'] = job.xpath(".//div[@class='result-card__contents job-result-card__contents']//time/text()").extract()[0]
            print(item['job_title'])
            yield item
