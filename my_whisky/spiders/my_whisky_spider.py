import scrapy


class MytrywhiskSpider(scrapy.Spider):
    name = 'mytrywhisk'
    allowed_domains = ['www.whiskyshop.com']
    start_urls = ['https://www.whiskyshop.com/gifts/whiskies-under-50']

    def parse(self, response):
        for item in response.css('.product-item-info'):
            yield{
                'brand' : item.css('.product-item-link::text').get(),
                'link' : item.css('.product-item-link::attr(href)').get(),
                'price' : item.css('.price::text').get()
            }
        
        next_page = response.css('.action.next::attr[href]')
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)