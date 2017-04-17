# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from base_proyecto.models import RegistroAltura
from base_proyecto.models import Estacion
from base_proyecto.models import EstadoTiempo
from unidecode import unidecode

class AlturasPipeline(object):
	DICT_ESTACIONES = {	
		'Manuel Diaz': 1338,
		'Cunapiru': 1339,
		'Borracho': 1484,
		'Novillos': 1523,
		'Coelho': 1526,
		'Laguna I': 1653, 
		'Las Toscas': 1613,
		'Laguna II': 1697,
		'Mazangano': 1617,
		'Aguiar': 1658,
		'Pereira': 1743,
		'Paso Las Piedras': 1741,
		'San Gregorio de Polanco': 1826,
		'Salsipuedes Ruta 20': 1819,
		'Paso de los Toros': 1915,
		'Lugo': 2153,
		'Sarandi del Yi': 2215,
		'Polanco del Yi': 2257,
		'Durazno': 2206,
		'Durazno Puente Viejo ': 3048,
		'Barra de Porongos': 2157,
		'Mercedes': 2145,
		'Villa Soriano': 2237
	}

	def process_item(self, item, spider):
		if spider.name not in ['alturas_ute']:
			return item
		altura = RegistroAltura(altura=item['altura'], fecha=item['fecha'], estacion_id=self.DICT_ESTACIONES['%s' %unidecode(item['lugar'])])
		altura.save()
		return item

class PrecipitacionesPipeline(object):
	# diccionario de esta chota
	DICT_ESTACIONES = {
		'UTE Baygorria': 1960,	
		'E.M. Bonete': 1963,	
		'Ansina': 1484,	
		'Picada de Coelho': 1526,	
		'Paso de las Toscas': 1613,	
		'Paso Mazangano': 1617,	
		'Paso Laguna': 1653,	
		'Laguna II': 1697,	
		'Paso Aguiar': 1658,	
		'Paso Pereira': 1743,	
		'Salsipuedes': 1819,	
		'San Gregorio': 1826,	
		'Manuel Diaz': 1338,	
		'Paso Las Piedras': 1741,	
		'Cunapiru': 1339,	
		'Barra de Porongos': 2157,	
		'Piedra Sola': 1558,	
		'Paso de los Novillos': 1523,	
		'Sarandi del Yi': 2215,	
		'Polanco del Yi': 2257,	
		'Paso de Lugo': 2153,	
		'E.M. Paso de los Toros': 1915,	
		'E.M. Palmar': 2052,	
		'E.M. Mercedes': 2145,	
		'E.M. Durazno': 2206,	
		'Villa Soriano': 2237,
	}
	def process_item(self, item, spider):
		if spider.name not in ['precipitaciones_ute']:
			return item
		estado_tiempo, created = EstadoTiempo.objects.get_or_create(estacion=Estacion.objects.get(id=self.DICT_ESTACIONES['%s' %unidecode(item['lugar'])]), fecha=item['fecha'])	
		estado_tiempo.precipitacion_mm = item['precipitacion']
		estado_tiempo.save()
		return item

class TuTiempoPipeline(object):

	DICT_ESTACIONES = {
		'Artigas': 3049,
		'BELLA UNION': 3050,
		'Carrasco': 3051,
		'Colonia': 3052,
		'Durazno': 3053,
		'FLORIDA': 3054,
		'LAGUNA DEL SAUCE': 3055,
		'YOUNG': 3056,
		'Treinta Y Tres': 3057,
		'Tacuarembo': 3058,
		'Salto': 3059,
		'ROCHA': 3060,
		'Rivera': 3061,
		'PUNTA DEL ESTE': 3062,
		'PRADO': 3063,
		'Paysandu': 3064,
		'PASO DE LOS TOROS': 3065,
		'Mercedes': 3066,
		'Melo': 3067,
		'Melilla': 3068,
		'Maldonado / Punta Est': 3069
	}

	def process_item(self, item, spider):
		if spider.name not in ['tiempo_tutiempo']:
			return item
		estado_tiempo, created = EstadoTiempo.objects.get_or_create(estacion=Estacion.objects.get(id=self.DICT_ESTACIONES['%s' %unidecode(item['lugar'])]), fecha=item['fecha'])	
		estado_tiempo.precipitacion_mm = item['precipitacion']
		estado_tiempo.max_temperatura = item['temp_maxima']
		estado_tiempo.min_temperatura = item['temp_minima']
		estado_tiempo.save()
		return item