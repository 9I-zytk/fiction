import scrapy
from urllib.parse import urljoin
from scrapy.http import Request
from fiction.items import FictionItem, FictionDetailItem
from fiction import util

# from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader


class biqugeSpider(scrapy.Spider):
    name = "biquge"
    allowed_domains = ["https://www.biquyun.com"]
    start_urls = ["https://www.biquyun.com/paihangbang/"]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # Create the loader using the response
        # l = ItemLoader(item=FictionItem(), response=response)
        next_selector = response.xpath('//*[@id="main"]//ul//a//@href')
        for num in range(0, 1):
            url = next_selector.extract()[num]
        # for url in next_selector.extract():
            yield Request(urljoin(response.url, url), callback=self.parse_dir_content)

    def parse_dir_content(self, response):
            l = ItemLoader(item=FictionItem(), response=response)
            l.add_xpath('title', '//*[@id="info"]//h1/text()')
            # 作者
            author = response.xpath('//*[@id="info"]//p/text()').extract_first()
            l.add_value('author', author.split('：')[1])
            # 最后更新时间
            latest = response.xpath('//*[@id="info"]//p[3]/text()').extract_first()
            l.add_value('latest', latest.split('：')[1])
            # latest_chapter
            latest_chapter = response.xpath('//*[@id="info"]//p[4]/a/text()').extract_first()
            l.add_value('latest_chapter', latest_chapter)
            # classify 分类
            classify = response.css('.con_top').extract_first()
            l.add_value('classify', util.remove_space(classify.split('&gt;')[1]))
            # 来源
            l.add_value('source', '笔趣阁')
            l.add_value('source_url', 'https://www.biquyun.com')
            # source_id
            l.add_value('source_id', util.get_source_id(response.url))
            l.add_value('url', response.url)
            # title_page
            title_page = response.xpath('//*[@id="fmimg"]//img/@src').extract_first()
            l.add_value('title_page', urljoin(response.url, title_page))
            # 简介
            next_selector = response.xpath('//*[@id="list"]//dl//a/@href')
            for num in range(0, 20):
                url = next_selector.extract()[num]
            # for url in next_selector.extract():
                yield Request(urljoin(response.url, url), callback=self.parse_chapter_content)
            yield l.load_item()

    def parse_chapter_content(self, response):
        l = ItemLoader(item=FictionDetailItem(), response=response)
        bookname = response.css('.bookname>h1').extract_first()
        l.add_xpath('contents', '//*[@id="content"]/text()')
        chapter = bookname.split(' ')[1]
        l.add_value('chapter', chapter)
        l.add_value('chapter_title', bookname.split(' ')[2])
        l.add_value('f_Id', util.get_source_id(response.url))
        yield l.load_item()

