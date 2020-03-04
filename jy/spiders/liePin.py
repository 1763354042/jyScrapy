# -*- coding: utf-8 -*-
import scrapy
from jy.items import JyItem
from scrapy.http.response.html import HtmlResponse
from urllib.parse import quote
from urllib.parse import unquote

class LiepinSpider(scrapy.Spider):
    name = 'liePin'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&d_sfrom=search_fp&key=%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91']
    jobType = ['Java', 'C++', 'PHP', '数据挖掘', 'C', 'C#', '.NET', 'Hadoop', 'Python',
               'Delphi', 'VB', 'Perl', 'Ruby', 'Node.js', '搜索算法', 'Golang', '推荐算法', 'Erlang',
               '算法工程师', '语音/视频/图形开发', '数据采集', 'UE4', '移动开发', 'HTML5', 'Android',
               'iOS', 'WP', '移动web前端', 'Flash开发', 'JavaScript', 'U3D', 'COCOS2DX', '测试工程师',
               '自动化测试', '功能测试', '性能测试', '测试开发', '移动端测试', '游戏测试', '硬件测试',
               '软件测试', '运维工程师', '运维开发工程师', '网络工程师', '系统工程师', 'IT技术支持',
               '系统管理员', '网络安全', '系统安全', 'DBA', '数据', 'ETL工程师', '数据仓库', '数据开发',
               '数据挖掘', '数据分析师', '数据架构师', '算法研究员', '项目经理', '项目主管', '项目助理',
               '项目专员', '实施顾问', '实施工程师', '需求分析工程师', '硬件', '嵌入式', '自动化', '单片机',
               '电路设计', '驱动开发', '系统集成', 'FPGA开发', 'DSP开发', 'ARM开发', 'PCB工艺', '射频工程师',
               '前端开发', 'web前端', 'JavaScript', 'Flash开发', 'HTML5', '', '通信技术工程师',
               '通信研发工程师', '数据通信工程师', '移动通信工程师', '电信网络工程师', '电信交换工程师',
               '有线传输工程师', '无线射频工程师', '通信电源工程师', '通信标准化工程师', '通信项目专员',
               '通信项目经理', '核心网工程师', '通信测试工程师', '通信设备工程师', '光通信工程师', '光传输工程师',
               '光网络工程师', '电子工程师', '电气工程师', 'FAE', '电气设计工程师', '高端技术职位', '技术经理',
               '技术总监', '测试经理', '架构师', 'CTO', '运维总监', '技术合伙人', '智能驾驶系统工程师',
               '反欺诈/风控算法', '人工智能', '自然语言处理', '机器学习', '深度学习', '语音识别', '图像识别',
               '算法研究员', '销售技术支持', '售前工程师', '售后工工程师']

    def parse(self, response):
         url = response.url
         url2Utf8 = unquote(url)
         firstKey2Url = quote('后端开发')
         keyWord = url2Utf8.split('key=')[-1].split('&')[0]
         jobList = response.xpath("//ul[@class = 'sojob-list']/li")
         for li in jobList:
            try:
                jobName = li.xpath(".//a/text()").get().strip()
                jobTxt = str(li.xpath(".//p[@class = 'condition clearfix']/@title")[0].get()).split('_')
                jobSalary = jobTxt[0]
                jobAddress = jobTxt[1]
                jobEducation = jobTxt[2]
                jobWorkYear = jobTxt[3]
                jobKey = keyWord
                jobCom = li.xpath(".//a/text()")[2].get()
                item = JyItem(jobName=jobName,jobEducation=jobEducation,jobWorkYear=jobWorkYear,jobCom=jobCom,
                           jobAddress=jobAddress,jobSalary=jobSalary,jobKey=jobKey)
                yield item
            except:
                continue
         next_url = response.xpath("//div[@class = 'pagerbar']/a/@href")[-2].get()
         print(next_url)
         if not next_url:
                return
         elif keyWord == '后端开发':     #后端开发先遍历所有关键词，然后进入下一页。如果不是后端开发，仅提取页面信息
             for job in self.jobType:
                new_url = url.replace(firstKey2Url,quote(job))
                print(new_url)
                yield scrapy.Request(new_url,callback=self.parse)
             yield scrapy.Request('https://www.liepin.com'+next_url,callback=self.parse)






