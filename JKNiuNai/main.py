from scrapy.cmdline import execute
import sys,os

f_dir = os.path.dirname(os.path.abspath(__file__))#获取当前目录的父目录
sys.path.append(f_dir)#把当前目录加入到环境变量
#execute(["scrapy","crawl","jobbole"])#执行命令 scrapy crawl jobbole
execute(["scrapy","crawl","jknn"])