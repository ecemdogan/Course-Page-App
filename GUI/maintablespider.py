import scrapy
import cardboarditem

class CardBodySpider(scrapy.Spider):
    name = "card-body"

    start_urls = ['http://eco.ieu.edu.tr/tr/syllabus/type/read/id/GEHU+203']

    def parse(self, response):
        self.logger.info('Card Body Spider')

        item = cardboarditem.CardBoardItem()

        tables = response.xpath("//div[@class='card-body']//div[@class='table-responsive']")
        item['course_name'] = tables[0].css('table div.editinput::text').get().strip()
        
        tables[0].css('table').get()
        tables[0].css('table div.editinput::text').get().strip()
        tables[1].xpath('string(table//tr[1]//td[3]//strong)').extract_first().replace('<br>','').strip()
        pass


