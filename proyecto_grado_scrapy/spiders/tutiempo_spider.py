
import scrapy
import re
import HTMLParser
import django
django.setup()

from proyecto_grado_scrapy.items import TiempoItem

from datetime import datetime


def starting_urls():
    base_url = 'http://www.tutiempo.net/clima/'
    list = []
    cities = [['Punta del Este', 865950], ['Artigas', 863300], ['Durazno', 865300],
              ['Bella_Union', 863150], ['Colonia', 865600], ['Carrasco', 865800],
              ['Florida', 865450], ['Laguna_del_Sauce', 865860], ['Melo', 864400],
              ['Mercedes', 864900], ['Melilla', 865750], ['Young', 864500], 
              ['Maldonado_Punta_Est', 865955], ['Paso_de_los_Toros', 864600],
              ['Prado', 865850], ['Paysandu', 864300], ['Rivera', 863500],
              ['Rocha', 865650], ['Salto', 863600], ['Tacuarembo', 863700],
              ['Treinta_Y_Tres', 865000]] 
    for city in cities:
        for x in range(1,12):
            if x < 10: 
                x_string = '0' + str(x)
            else:
                x_string = str(x)
            for y in range(1970, 2017):
                list.append(base_url + city[0] + '/' + x_string + '-' + str(y) + '/' + str(city[1]) + '.htm') 
    return list

class TiempoItemSpider(scrapy.Spider):
    name = "tiempo_tutiempo"
    allowed_domains = ["www.tutiempo.net"]
    start_urls = [
        starting_urls
    ]


    def parse(self, response):
        lugar = response.xpath('//h2/text()').extract()[0].replace('Clima ', '')     
        table_med = response.xpath('//table[@class="medias mensuales"]//tr')
        table_med.pop(0)
        table_med.pop(len(table_med)-1)
        table_med.pop(len(table_med)-1)
        for tr in table_med:
            item = TiempoItem()
            item['temp_maxima'] = tr.xpath('td[3]//text()').extract()[0].replace('-', '')
            item['temp_minima'] = tr.xpath('td[4]//text()').extract()[0].replace('-', '') 
            item['precipitacion'] = tr.xpath('td[7]//text()').extract()[0].replace('-', '')
            if bool(item['temp_minima']) & bool(item['temp_maxima']) & bool(item['precipitacion']): 
                yield item
