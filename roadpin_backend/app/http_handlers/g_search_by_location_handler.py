# -*- coding: utf-8 -*-

from app.constants import S_OK, S_ERR
import random
import math
import base64
import time
import ujson as json

from app.constants import EARTH_EQUATOIAL_CIRCUMFERENCE, EARTH_MERIDIONAL_CIRCUMFERENCE

from app import cfg
from app import util

def g_search_by_location_handler(params):
    lat = util._int(params.get('lat', 25))
    lon = util._int(params.get('lng', 121))

    dist = util._int(params.get('distance', 10))
    dist = max(dist, 10)

    dist_x = 360 * dist / EARTH_EQUATOIAL_CIRCUMFERENCE
    dist_y = 360 * dist / EARTH_MERIDIONAL_CIRCUMFERENCE

    min_x = lon - dist_x
    max_x = lon + dist_x
    min_y = lat - dist_y
    max_y = lat + dist_y

    query = {'geo': {'$geoWithin': {'$geometry': {'type': 'Polygon', 'coordinates': [[[min_x, min_y], [min_x, max_y], [max_x, max_y], [max_x, min_y], [min_x, min_y]]]}}}}

    results = util.db_find('roadDB', query)
    return results