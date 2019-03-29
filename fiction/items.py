# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class FictionItem(Item):
    # define the fields for your item here like:
    # fiction 小说
    # 书流水号
    recId = Field()
    # 书名
    title = Field()
    # 作者
    author = Field()
    # 简介
    introduction = Field()
    # 分类
    classify = Field()
    # 章节
    chapter_count = Field()
    # 最近更新章节
    latest_chapter = Field()
    # 来源网站
    source = Field()
    # 来源网站书名编号
    source_id = Field()
    # 来源网站链接
    source_url = Field()
    # 最后更新时间
    latest = Field()
    # 状态: 连载/完结
    status = Field()
    # 封面
    title_page = Field()
    # 总字数
    word_count = Field()
    # 书链接
    url = Field()


class FictionDetailItem(Item):
    # 书详细内容
    recId = Field()
    # 书ID
    f_Id = Field()
    # 章节
    chapter = Field()
    # 章节名
    chapter_title = Field()
    # 内容
    contents = Field()
    # 最后更新时间
    update = Field()
