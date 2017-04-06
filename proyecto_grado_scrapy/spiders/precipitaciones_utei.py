
import scrapy
import re
import HTMLParser
import django
django.setup()

from proyecto_grado_scrapy.items import PrecipitacionItem

from datetime import datetime


class PrecipitacionesItemSpider(scrapy.Spider):
    name = "precipitaciones_ute"
    allowed_domains = ["www.ute.com.uy"]
    start_urls = [
        "http://www.ute.com.uy/Novedades/Lluvias/precipitacionesocurridaprevisiondeniveles.htm"
    ]

    def parse(self, response):

        # Obtengo la primer fila de la tabla de precipitaciones, en la misma se encuentran los lugares
        fila_lugares = response.xpath("//table[@id = 'ctl00_ContentPlaceHolder1_gridPrecipTotales']//tr/th/font/b/text()")
        lugares = []
        for fila in fila_lugares:
            lugares.append(fila.extract())

        fila_precipitaciones = response.xpath("//table[@id = 'ctl00_ContentPlaceHolder1_gridPrecipTotales']//tr[1]/td/font/text()")
        precipitaciones = []
        for fila in fila_precipitaciones:
            precipitaciones.append(fila.extract())

        for index, lugar in enumerate(lugares):
            precipitacion_date = datetime.strptime(precipitaciones[0], '%d/%m/%Y')

            if index != 0 and index != 1:
                item = PrecipitacionItem()
                item['lugar'] = lugar.replace('(mm)','')
                item['fecha'] = precipitacion_date
                try:
                    item['precipitacion'] = float(precipitaciones[index].replace(',','.'))
                except ValueError:
                    item['precipitacion'] = None
                yield item
