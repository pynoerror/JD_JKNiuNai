# -*- coding: utf-8 -*-
import scrapy
from JKNiuNai.items import JKNiuNaiItem
from urllib import parse
import json

class JKNNSpider(scrapy.Spider):
    name = 'jknn'
    start_urls = ['https://search.jd.com/Search?keyword=%E8%BF%9B%E5%8F%A3%E7%89%9B%E5%A5%B6&enc=utf-8&wq=%E8%BF%9B%E5%8F%A3%E7%89%9B%E5%A5%B6&pvid=928b86238c194219afbaf03a5ab84aad']
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cookie':' shshshfpa = 04678bba - 6a34 - 3c9c - 5d2a - 8c9120f94457 - 1529487111;shshshfpb = 13d8c73945ca14076aec04c496fb39b4059803865255012035b2a1f06e;qrsc = 3;pinId = CoJot0aNXE_MK_HrUqujKLV9 - x - f3wj7;TrackID = 1hBtrEJKUn - KzNVX8naEiMixMcDbuX1QBn21qaKi_hKxDDTwrxx8pDJ6etl6fQY3h56rZxX0Gr7iLHUFIVS4ICpAsNPisP9qd_OKkIyELQtA;xtest = 7320.cf6b6759;__jdu = 1745316852;__jdc = 122270672;rkv = V0700;unpl = V2_ZzNtbUpWRxV8CEIAKR8LAWILEA8SUhMSJQgRUXMaCQNhC0ZVclRCFX0UR1FnGVoUZwIZXURcRh1FCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHsfWQFlAxVURlRzJXI4dmR5H1kFbgYiXHJWc1chVEFVfhxVDCoDFFhGVUMSfAxFZHopXw % 3d % 3d;__jdv = 122270672 | baidu - pinzhuan | t_288551095_baidupinzhuan | cpc | 0f3d30c8dba7459bb52f2eb5eba8ac7d_0_9051815ec7f5493ca4a6a1f492d779e9 | 1555467469167;_gcl_au = 1.1.1316332854.1555483171;mt_xid = V2_52007VwMUV1laUl0WTRpsBGMAEgFZXVdGHx4eCRliVEZWQVBQDhpVGVsDblRHAF9RAVIXeRpdBW8fE1dBWFRLH0wSWQRsBhNiX2hSahxPGlgMZwsVW21YV1wY;__jda = 122270672.1745316852.1529486288.1555483172.1555571670.64;areaId = 1;ipLoc - djd = 1 - 2801 - 0 - 0;shshshfp = 9beb28a9f1600c35b0eb5baf70edc189;3AB9D23F7A4B3C9B = HJ7STDGJH65Y52FU2MKSTWJEZBYAHLLQ3EDAGPSIU2VTKECK3V35GTUJY5U2PDL24NG6FWRXGVRYPRFNBJBPHF5V6Q; __jdb = 122270672.5.1745316852 | 64.1555571670;shshshsID = 9bb7ca102dcc7785a69858d019e04bec_4_155557192951',
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko)Chrome / 69.0.3497.100Safari / 537.36'
    }

    # 获取评论数
    def get_comment(self,response):
        item = response.meta["item"]
        js = json.loads(str(response.text)) #json转字典
        item['commentcount'] = js['CommentsCount'][0]['CommentCountStr']    #全部评论数
        item['videocount'] = js['CommentsCount'][0]['VideoCountStr']    #视频晒单
        item['aftercount'] = js['CommentsCount'][0]['AfterCountStr']    #追评
        item['goodcount'] = js['CommentsCount'][0]['GoodCountStr']  #好评
        item['generalcount'] = js['CommentsCount'][0]['GeneralCountStr']    #中评
        item['poorcount'] = js['CommentsCount'][0]['PoorCountStr']  #差评
        yield item

    #爬取第一页展示的商品：
    def parse(self, response):
        goods = response.css("#J_goodsList ul li.gl-item")
        for good in goods:
            item = JKNiuNaiItem()
            item["id"] = good.css("::attr(data-sku)").extract()[0]
            item["name"] = "".join(good.css(".p-name em::text").extract())
            item["shop_name"] = good.css(".curr-shop ::text").extract()
            url = good.css(".p-img a::attr(href)").extract()
            item["link"] = parse.urljoin("http:",url=url[0])
            class_price = "J_" + item["id"]
            item["price"] = good.css("."+ class_price +" i::text").extract()[0]
            item["price_plus"] = good.css(".price-plus-1 em::text").extract()#会员价
            comment = "J_comment_"+ item["id"]
            url_commet = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds="+ item["id"]
            yield scrapy.Request(url_commet,meta={"item":item},headers=self.headers, callback=self.get_comment)

