# -*- coding: utf-8 -*-

import vmapper
import os
os.environ['USE_PYGEOS'] = '0'
import geopandas

def test_pd():
    import pandas as pd
    pass

def test_gpd():
    ## a test with point, polylines, and polygons shapefile
    import geopandas as gpd
    gdf1 = gpd.read_file('testdata/county.shp')
    gdf2 = gpd.read_file('testdata/rail_way.shp', encoding='big5')
    gdf2 = gdf2.to_crs(gdf1.crs)
    gdf3 = gpd.read_file('testdata/rail_station.shp', encoding='utf-8')
    gdf3 = gdf3.to_crs(gdf1.crs)
    m = vmapper.Map(interactive=True)
    m.add_geodataframe(gdf1, layername='township', draw_setting=dict(labelby='countyname', idby='countyid'), hovercolor=(255,10,10),hoveropacity=0.9,hoverstroke="#FF0",hoverswidth=1, color=(20,20,250), opacity=0.6, strokecolor="#0F0", strokewidth=30, showlabel=True)
    m.add_geodataframe(gdf2, layername='railway', draw_setting=dict(labelby='railcode', idby='railid'),strokecolor="#FF7",  hoverstroke="#0F0",hoverswidth=500, strokewidth=300, showlabel=True)
    m.add_geodataframe(gdf3, layername='railstation', draw_setting=dict(labelby='landmarkna', idby='landmarkid'), radius=200, hovercolor=(255,255,10),hoveropacity=0.9,hoverstroke="#FFF",hoverswidth=50, color=(255,20,250), opacity=0.6, strokecolor="#000", strokewidth=10, showlabel=True)
    m.add_title('testing title')
    m.export_to_file('testdata/output/testing1b.svg')

if __name__ == '__main__':
    test_gpd()
    #test_pd()
