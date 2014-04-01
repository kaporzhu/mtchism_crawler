# -*- coding: utf-8 -*-
from scrapy.item import Item, Field


class FoodItem(Item):
    """
    Food item
    """
    name = Field()
    category_name = Field()
    heat = Field()  # 热量（大卡）
    carbohydrate = Field()  # 碳水化合物（克）
    fat = Field()  # 脂肪（克）
    protein = Field()  # 蛋白质（克）
    cellulose = Field()  # 纤维素（克）
