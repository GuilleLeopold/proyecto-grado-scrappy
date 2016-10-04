
import scrapy
import re
import HTMLParser
import django
django.setup()

from proyecto_grado_scrapy.items import AlturaItem

from datetime import datetime


class AlturaItemSpider(scrapy.Spider):
    name = "alturas_ute"
    allowed_domains = ["www.ute.com.uy"]
    start_urls = [
        "http://www.ute.com.uy/SgePublico/ConsSATAlturas.aspx"
    ]

    def parse(self, response):

        # Obtengo la primer fila de la tabla de alturas, en la misma se encuentran los lugares
        fila_lugares = response.xpath("//table[@id = 'ctl00_ContentPlaceHolder1_gridAportes']//tr/th/font/b/text()")
        lugares = []
        for fila in fila_lugares:
            lugares.append(fila.extract())

        fila_alturas = response.xpath("//table[@id = 'ctl00_ContentPlaceHolder1_gridAportes']//tr[3]/td/font/text()")
        alturas = []
        for fila in fila_alturas:
            alturas.append(fila.extract())

        for index, lugar in enumerate(lugares):
            altura_date = datetime.strptime(alturas[0], '%d/%m/%Y')

            if index != 0 and index != 1:
                item = AlturaItem()
                item['lugar'] = lugar.replace('(m)','')
                item['fecha'] = altura_date
                try:
                    item['altura'] = float(alturas[index].replace(',','.'))
                except ValueError:
                    item['altura'] = None
                yield item
