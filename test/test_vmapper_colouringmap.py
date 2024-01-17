 # -*- coding: utf-8 -*-

from colouringmap import theme_mapping as tm
import vmapper

import pandas as pd
import geopandas as gpd
from shapely.ops import cascaded_union

def test_africa_map():
    gdf = gpd.read_file('/media/benny/data/GIS_folder/TM_WORLD_BORDERS_SIMPL-0.3/TM_WORLD_BORDERS_SIMPL-0.3.shp')

    gdf = gdf[gdf.REGION==2]
    print(gdf.head())

    gdf = gdf.to_crs({'init': 'epsg:3410'})

    geoms = gdf.geometry.tolist()
    areas = [ g.area for g in geoms ]

    pop = gdf.POP2005.tolist()
    popdens = [ float(p*1000000.)/a for p,a in zip(pop,areas) ]
    gdf['popdens'] = popdens

    gdf = gdf.to_crs({'init': 'esri:54009'}) #World Mollweide

    level_list, colour_list, colour_tuples = tm.colouring_sequence(gdf, colorbysequence='popdens', break_method='natural_break', break_N=7, color_group='cmocean_sequential', color_name='Turbid_10')

    gdf['level'] = level_list
    gdf['colors'] = colour_list

    m = vmapper.Map(interactive=True) ## interactive will use the SVGPan.js, which will be copy automatically

    m.add_geodataframe(gdf, layername='country', draw_setting=dict(labelby='NAME', idby='FIPS', colorby='colors'),  hovercolor=(255,10,10),hoveropacity=0.9,hoverstroke="#FF0",hoverswidth=1, color=(20,20,250), opacity=0.6, strokecolor="#0F0", strokewidth=30, showlabel=True)

    m.export_to_file('testing_africa_map.svg')

def test_taipei_crime_map():
    gdf = gpd.read_file('/media/benny/data/GIS_folder/newWorspaces/GISfolder/vil_67_N_C.shp')
    #print gdf.head()

    aa = gdf.area.tolist()
    cc = gdf.NUMPOINTS.tolist()
    cdens = [ c*10000/a for c,a in zip(cc,aa) ]
    gdf['cdens'] = cdens
    level_list, colour_list, colour_tuples = tm.colouring_sequence(gdf, colorbysequence='cdens', break_method='natural_break', break_N=7, color_group='cmocean_sequential', color_name='Turbid_10')
    print(colour_tuples)

    cn = gdf.countyname.tolist()
    tn = gdf.townname.tolist()
    vn = gdf.villagenam.tolist()
    namelab = [ c+t+v+':count='+str(n) for c,t,v,n in zip(cn,tn,vn,cc) ]
    gdf['nlabel'] = namelab
    gdf['level'] = level_list
    gdf['colour'] = colour_list

    tnset = list(set(tn))
    t_geom = []
    for t in tnset:
        temp = gdf[gdf['townname']==t]
        temp_g = temp['geometry'].tolist()
        town_bound = cascaded_union(temp_g)
        t_geom.append(town_bound)
    tdf = pd.DataFrame.from_dict(dict(tname=tnset))
    tgdf = gpd.GeoDataFrame(tdf, geometry=t_geom, crs=gdf.crs)

    print(tgdf.head())
    m = vmapper.Map(interactive=True) ## interactive will use the SVGPan.js, which will be copy automatically

    m.add_geodataframe(tgdf, layername='township', opacity=1., strokewidth=50, strokecolor='#000', color='transparent')

    m.add_geodataframe(gdf, layername='crime_density', draw_setting=dict(labelby='nlabel', idby='VILLCODE', colorby='colour'),  hovercolor=(255,10,10),hoveropacity=0.9,hoverstroke="#FF0",hoverswidth=1, color=(50,50,50), opacity=0.7, strokecolor="#FFF", strokewidth=10, showlabel=True)

    m.add_title('Taipei area crime density')
    m.add_footer('Proudly powered by vmapper and colouringmap.')
    m.add_color_legend(colour_tuples, layername='Crime density per 10000 people')

    m.export_to_file('testing_taipei_crime_map2.svg')


if __name__ == '__main__':
    test_taipei_crime_map()
