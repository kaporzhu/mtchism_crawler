# Scrapy settings for mtchism_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'mtchism_crawler'

SPIDER_MODULES = ['mtchism_crawler.spiders']
NEWSPIDER_MODULE = 'mtchism_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mtchism_crawler (+http://www.yourdomain.com)'

ITEM_PIPELINES = [
    'mtchism_crawler.pipelines.FoodPipeline',
]

LOG_LEVEL = 'INFO'
