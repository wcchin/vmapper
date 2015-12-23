# -*- coding: utf-8 -*-
"""
Created on Sun Nov 23 23:06:19 2014

@author: benny
"""

from kartograph import Kartograph
import xml.etree.ElementTree as ET

K = Kartograph()
#('postgresql://postgrebenny:B3nnychin@140.112.64.62:5432/citygraph')
#config={ "layers": { "mylayer": { "src": "postgis:{'host':'140.112.64.62', 'port':'5432', 'dbname':'postgres', 'user':'postgrebenny', 'password':'B3nnychin'}", "table": "township_seudata_84_3", "bounds": {"mode": "polygon"}}}}

#"proj": {"id": "laea","lon0": 121.25,"lat0": 25.05},
config={ "layers": { "mylayer": { "src": "ne_50m_admin_0_countries.shp" } } }
aa = K.generate(config)
bb = str(aa).replace("'", "\"").replace('<?xml version="1.0" ?><!DOCTYPE svg  PUBLIC "-//W3C//DTD SVG 1.1//EN"  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">','')
print bb

"""
root = ET.fromstring(str(aa))
print str(aa)
for child in root:
    print child.tag, child.attrib
"""