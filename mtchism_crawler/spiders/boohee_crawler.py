# -*- coding: utf-8 -*-
import re

from scrapy.http.request import Request
from scrapy.spider import Spider

from bs4 import BeautifulSoup
from mtchism_crawler.items import FoodItem


class BooheeSpider(Spider):
    """
    Boohee food info spider
    """
    name = 'boohee'
    allowed_domains = ['boohee.com']
    start_urls = [
        'http://www.boohee.com/food/view_group/1',
    ]

    def parse(self, response):
        """
        Parse response
        """
        soup = BeautifulSoup(response.body, 'lxml')

        # check if it's a valid page
        if not soup.find(class_='food-list'):
            yield None

        # check if there is next page
        next_page = soup.find('a', class_='next_page')
        if next_page:
            yield Request('http://www.boohee.com{}'.format(next_page['href']))
#         else:
#             # no more page for this group, goto next group
#             group_id = re.match('.*view_group/(\d*)', response.url).group(1)
#             next_group_id = int(group_id) + 1
#             next_group_url = 'http://www.boohee.com/food/view_group/{}'.format(next_group_id)  # noqa
#             yield Request(next_group_url)

        # parse foods
        for food in soup.select('.food-list'):
            food_url = 'http://www.boohee.com{}'.format(
                food.find(class_='illus').a['href'])
            yield Request(food_url, self.parse_food)

    def parse_food(self, response):
        """
        Parse food details
        """
        soup = BeautifulSoup(response.body, 'lxml')
        field_titles = {
            u'热量(大卡)': 'heat',
            u'碳水化合物(克)': 'carbohydrate',
            u'脂肪(克)': 'fat',
            u'蛋白质(克)': 'protein',
            u'纤维素(克)': 'cellulose'
        }
        food = FoodItem()
        header = soup.find(class_='crumb')
        food['category_name'] = header.select('a')[1].text.strip()
        [a.decompose() for a in header.select('a')]
        food['name'] = header.text.strip(u'\xbb \n')
        for dd in soup.select('.nutr-tag dd'):
            title = dd.find(class_='dt').text.strip()
            value = dd.find(class_='dd').text.strip()
            if title in field_titles:
                if value == u'\u4e00':
                    value = -1
                food[field_titles[title]] = float(value)
        yield food
