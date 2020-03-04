# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JyPipeline(object):
    def open_spider(self,spider):
        print('+'*30)

    def save_to_mysql(self,data):
        db = pymysql.connect("localhost", "root", "root", "pc20")
        sql = 'insert into dataPosition (keyWord,address,company,position,salary,workYear,education)' \
              ' values ' + data + ';'  # data为传入字符串，在最后以";"结尾
        cursor = db.cursor()
        cursor.execute(sql)  # 执行sql语句，返回sql查询成功的记录数目,我只在表中插入一条记录，查询成功最多所以也就一条记录数
        db.commit()
        db.close()
        print(sql)

    def process_item(self, item, spider):
        item_dict = dict(item)
        sqlStr = "('" + item_dict['jobKey']+"','"+item_dict['jobAddress']+"','"+item_dict['jobCom']+"'" \
                ",'"+ item_dict['jobName']+"','"+item_dict['jobSalary']+"','"+item_dict['jobWorkYear']+"'" \
                ",'"+item_dict['jobEducation']+"')"
        print(sqlStr)
        self.save_to_mysql(sqlStr)
        return item

    def close_spider(self,spider):
        print('='*30)
