# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
# http://stackoverflow.com/questions/19068308/access-django-models-with-scrapy-defining-path-to-django-project read here

import scrapy

from scrapy.item import Item, Field

class AlturaItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    altura = scrapy.Field()
    lugar = scrapy.Field()
    fecha = scrapy.Field()

class PrecipitacionItem(Item):
	precipitacion = scrapy.Field()
	lugar = scrapy.Field()
	fecha = scrapy.Field()

class TiempoItem(Item):
	precipitacion = scrapy.Field()
	temp_maxima = scrapy.Field()
	temp_minima = scrapy.Field()
	lugar = scrapy.Field()
	fecha = scrapy.Field()