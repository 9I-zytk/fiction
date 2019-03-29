# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
from fiction import sql
from fiction.items import FictionItem, FictionDetailItem

class FictionPipeline(object):
    def __init__(self):
        self.file = codecs.open('fiction.json', 'w', encoding='utf-8')

    # @ classmethod
    # def from_crawler(cls, crawler):  # 生成pipeline实例的方法
    #     pipeline = cls()
    # 将spider_opened连接到信号上，当spider打开时执行spider_opened方法
    #     crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
    #     crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
    #     return pipeline
    #
    # def spider_opened(self, spider):  #
    #     file = open('%s_ip.json' % spider.name, 'w+b')  # 生成文件描述符
    #     self.files[spider] = file  # 保存描述符的引用
    #     self.exporter = JsonLinesItemExporter(file)  # 实例化一个Exporter类
    #     self.exporter.start_exporting()  # 开始输出
    #
    # def spider_closed(self, spider):
    #     self.exporter.finish_exporting()  # 结束输出
    #     # print('*'*50)
    #     file = self.files.pop(spider)
    #     # print(file.name)
    #     file.close()

    def process_item(self, item, spider):
        # lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.file.write(lines)
        print(isinstance(item, FictionItem))
        return item

    def process_item_fiction(self, item):
        pass

    @staticmethod
    def spider_closed(self, spider):
        sql.dis_connect()
