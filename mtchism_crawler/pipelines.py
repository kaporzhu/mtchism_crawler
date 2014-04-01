# -*- coding: utf-8 -*-
import os
from datetime import datetime

from scrapy import signals
from scrapy.contrib.exporter import JsonItemExporter
from scrapy.xlib.pydispatch import dispatcher


class FoodPipeline(object):
    """
    Pipeline for food item.
    Export food data to the json file
    """

    def __init__(self):
        dispatcher.connect(self.spider_opened, signals.spider_opened)
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_opened(self, spider):
        """
        Spider open handler
        """
        time_now_str = datetime.strftime(datetime.now(), '%Y_%m_%d_%H_%M_%S')
        filename = '{}_{}.json'.format(spider.name, time_now_str)
        f = open(os.path.join('data', filename), 'w+')
        self.exporter = JsonItemExporter(f)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        """
        Spider close handler
        """
        self.exporter.finish_exporting()
        self.exporter.file.close()

    def process_item(self, item, spider):
        """
        Process each food item
        """
        self.exporter.export_item(item)
        return item
