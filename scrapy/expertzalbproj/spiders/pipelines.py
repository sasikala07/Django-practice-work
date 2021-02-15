# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.exceptions import DropItem
import re

##pipeline

class ExpertproPipeline:
    def process_item(self, item, spider):
        vals=re.findall(r"Python", str(item['desc']))  ##using reg exp for getting particualr content
        print("Pipe line executed = ", vals)
        if (len(vals)>0):
            item['desc'] = ""
            return item
        else:
            raise DropItem()

