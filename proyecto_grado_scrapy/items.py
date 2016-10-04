# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
# http://stackoverflow.com/questions/19068308/access-django-models-with-scrapy-defining-path-to-django-project read here

import scrapy

from scrapy_djangoitem import DjangoItem
from scrapy.item import Field

from scrapy_ute.models import Altura

class AlturaItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = Altura
