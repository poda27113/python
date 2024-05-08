import scrapy

from scrapy.crawler import CrawlerProcess

class NGOSpider(scrapy.Spider):
    name = 'ngo_spider'
    start_urls = [
        'https://www.google.com/search?q=medical+NGO+USA'
    ]

    def parse(self, response):
        region = response.url.split('-')[-1]  # Extract region from URL
        ngos = response.xpath('//div[@class="ngo"]')  # Adjust the XPath according to the structure of NGO pages
        with open(f'ngos_{region}.txt', 'a') as f:  # Open file in append mode
            for ngo in ngos:
                name = ngo.xpath('.//h2/text()').get()
                email = ngo.xpath('.//span[contains(@class, "email")]/text()').get()
                state = ngo.xpath('.//span[contains(@class, "state")]/text()').get()
                website = ngo.xpath('.//a[contains(@class, "website")]/@href').get()
            
             # Write data to file
                f.write(f"Region: {region}\n")
                f.write(f"state: {state}\n")
                f.write(f"Name: {name}\n")
                f.write(f"Email: {email}\n")
                f.write(f"Website: {website}\n\n")
        
process = CrawlerProcess(
    settings={
    'USER_AGENT': 'Mozilla/5.0',
    'ROBOTSTXT_OBEY': True
}
)
process.crawl(NGOSpider)
process.start()
