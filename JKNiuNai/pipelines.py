# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

class JkniunaiPipeline(object):

    wd = Workbook()
    ws = wd.active
    ws.append(["商品ID","商品名称","店铺名称","商品链接","商品价格","会员价格","全部评论数","视频晒单","追评","好评","中评","差评"])
    def process_item(self, item, spider):
        for key, value in item.items():
            if value == []:
                item[key] = ""
            elif type(value) == list:
                item[key] = "".join(value)
            else:
                pass
        line = [item["id"],item["name"],item["shop_name"],item["link"],item["price"],item["price_plus"],item['commentcount'],
                item['videocount'],item['aftercount'],item['goodcount'],item['generalcount'],item['poorcount']]
        self.ws.append(line)
        self.wd.save("D:\pycharm\进口牛奶.xlsx")
        return item
