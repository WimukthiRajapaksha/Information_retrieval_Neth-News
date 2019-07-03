import scrapy


class SinhalaNewsSpider(scrapy.Spider):
    name = "SinhalaNews"
    start_urls = [
            'http://nethnews.lk/category/5'
    ]

    #def start_requests(self):
     #   url = 'http://nethnews.lk/category/5'
      #  for i in range(1, 5, 1):
       #     url = url + '?page=' + i
        #yield scrapy.Request(url, self.parse)
        

    def parse(self, response):
        #item = defaultdict(list)
        for quote in response.css('div.content_left div.breaking_news'):
            linkedPage = response.urljoin(quote.css('.entry-title a::attr(href)').extract()[0])
            description = scrapy.http.HtmlResponse(linkedPage)
            print('\n\n------------------------++++++++++++++++++++\n\n')
            #for a in description.css('div.td-post-content'):
            #for a in description:
            print(description)
         #   for quo in description.css('div.td-post-content'):
          #      print(quo.css('p::text').getall())
                #abc.add(quo.css('p::text').getall())
                #print(abc)
            print('\n\n-----------------------------------\n\n')
            dateInfo = {
                'year': quote.css('div.col-sm-9 div.gossip_publish_div div.publish_date::text').get().strip().split('-')[0],
                'month': quote.css('div.col-sm-9 div.gossip_publish_div div.publish_date::text').get().strip().split('-')[1],
                'date': quote.css('div.col-sm-9 div.gossip_publish_div div.publish_date::text').get().strip().split('-')[2]
            }
            yield {
                'title': quote.css('div.col-sm-9 h3.entry-title a::text').get().strip(),
                'posted on': dateInfo,
                'views': quote.css('div.col-sm-9 div.gossip_publish_div div.td-post-views::text').extract()[-1].strip(),
                'description': description
            }
            # scrapy.Request(linkedPage, self.parse_page)


        next_page = response.css('ul.pagination li a::attr(href)')[-1].extract()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_page(self, response):
        abc = ''
        for quotee in response.css('div.td-post-content'):
            print(quotee.css('p::text').getall())
            abc.add(quotee.css('p::text').getall())
        print(abc)
        return abc
