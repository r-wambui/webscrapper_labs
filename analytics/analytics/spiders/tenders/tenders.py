# pylint: disable=import-error
import json
import scrapy
import re

class Myjobmag(scrapy.Spider):
    """ Scrape tenders data from the government web portal """

    name = "tenders"
    collection_name = "tenders"

    def start_requests(self):
        """ Fetching data from API """
        url = 'https://www.tenders.go.ke/website/tenders/advancedSearchFilter/open?'\
            'org_type&org_name&tender_category&tender_type&draw=1&columns%5B0%5D%5Bdata%5D'\
            '=type&columns%5B0%5D%5Bname%5D=organizations.type&columns%5B0%5D%5Bsearchable%5D'\
            '=true&columns%5B0%5D%5Borderable%5D=true&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D'\
            '&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=org_name&'\
            'columns%5B1%5D%5Bname%5D=organizations.name&columns%5B1%5D%5Bsearchable%5D=true&'\
            'columns%5B1%5D%5Borderable%5D=true&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D&columns%5'\
            'B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=tender_ref_no&columns%5B'\
            '2%5D%5Bname%5D=tender_notices.tender_ref_no&columns%5B2%5D%5Bsearchable%5D=true&columns%'\
            '5B2%5D%5Borderable%5D=true&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D&columns%5B2%5D%5Bsearch%5D'\
            '%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=tender_title&columns%5B3%5D%5Bname%5D=tender_notices'\
            '.tender_title&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&'\
            'columns%5B3%5D%5Bsearch%5D%5Bvalue%5D&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%'\
            '5B4%5D%5Bdata%5D=tender_category&columns%5B4%5D%5Bname%5D=tender_notices.tender_category&'\
            'columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch'\
            '%5D%5Bvalue%5D&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=tender_type&'\
            'columns%5B5%5D%5Bname%5D=tender_notices.tender_type&columns%5B5%5D%5Bsearchable%5D=true&columns%'\
            '5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D&columns%5B5%5D%5Bsearch%5D%'\
            '5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=tender_status&columns%5B6%5D%5Bname%5D=tender_notices.'\
            'tender_status&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%'\
            '5B6%5D%5Bsearch%5D%5Bvalue%5D&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%'\
            '5D=closing_date&columns%5B7%5D%5Bname%5D=tender_notices.closing_date&columns%5B7%5D%5Bsearchable%5D'\
            '=true&columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D&columns%'\
            '5B7%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=0&order%5B0%5D%5Bdir%5D=asc&'\
            'start=0&length=300&search%5Bvalue%5D&search%5Bregex%5D=false&_=1593598282595&input'
        
        # work on the pagination
        yield scrapy.Request(url=url, callback=self.get_tenders)
    
    def get_tenders(self, response):
        item = {}
        response_data = json.loads(response.body)['data']
        for row in response_data:
            item['tender_code'] = row['tender_code']
            item['tender_type'] = row['tender_type']
            item['org_name'] = row['org_name']
            item['tender_title'] = row['tender_title']
            item['tender_reference_no'] = (re.findall(r'(?<=<a href=")[^"]*',row['tender_ref_no']))[0]
            item['publication_date'] = row['publication_date']
            item['closing_date'] = row['closing_date']
            yield item
