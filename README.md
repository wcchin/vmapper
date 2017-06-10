# vmapper
Vector MAP ProducER - a simple python library for creating SVG map in python

### intro 
This is a simple python library for creating map in python, from reading spatial data source to exporting map.

It has been more than a year since the last commit. I have tried to use this in my other analysis projects. 
After a series of modifications according to different projects' needs, I decided to restructure this vmapper package, and changed the aims to be more simple.

Now, the vmapper package aims to create svg maps from a geodataframe, or a dataframe with x and y coordinates. 
A series of settings can be pass into vmapper for modifying the features looks, using the draw_setting variable, e.g. the coordinates columns, the color columns (which should be the color hexcode). 


### dependencies
- jinja2
- pandas
- geopandas

### install

this package is in alpha, so it is a good idea to install in editable mode (-e)
```sh
git clone https://github.com/wcchin/vmapper.git
cd vmapper/
pip install -e .

```

or 

```sh
pip install -e git+https://github.com/wcchin/vmapper.git#egg=vmapper

```

### usage

```python
## import geopandas
import geopandas as gpd

## reading files (labels in chinese)
gdf1 = gpd.read_file('testdata/county.shp') ## a polygon file, encoding is utf-8, projection Twd1997/TM2
gdf2 = gpd.read_file('testdata/rail_way.shp', encoding='big5') ## a polyline files, the encoding is big5, projection in wgs84
gdf2 = gdf2.to_crs(gdf1.crs) ## reproject to the same as gdf1
gdf3 = gpd.read_file('testdata/rail_station.shp', encoding='utf-8') ## a point file, encoding utf-8, projection wgs84
gdf3 = gdf3.to_crs(gdf1.crs) ## reproject to the same as gdf1

## start making map, starting by creating a blank map
m = vmapper.Map(interactive=True) ## interactive will use the SVGPan.js, which will be copy automatically

## add the gdf into the map, check the draw_setting
m.add_geodataframe(gdf1, layername='township', draw_setting=dict(labelby='countyname', idby='countyid'), hovercolor=(255,10,10),hoveropacity=0.9,hoverstroke="#FF0",hoverswidth=1, color=(20,20,250), opacity=0.6, strokecolor="#0F0", strokewidth=30, showlabel=True)
m.add_geodataframe(gdf2, layername='railway', draw_setting=dict(labelby='railcode', idby='railid'),strokecolor="#FF7",  hoverstroke="#0F0",hoverswidth=500, strokewidth=300, showlabel=True)
m.add_geodataframe(gdf3, layername='railstation', draw_setting=dict(labelby='landmarkna', idby='landmarkid'), radius=200, hovercolor=(255,255,10),hoveropacity=0.9,hoverstroke="#FFF",hoverswidth=50, color=(255,20,250), opacity=0.6, strokecolor="#000", strokewidth=10, showlabel=True)

## finally, export the map to a file
m.export_to_file('testdata/output/testing1b.svg')

```

### sample output
The following map is generated using vmapper, the color of each polygon feature is assigned using <a href="https://wcchin.github.io/colouringmap" target="blank">colouringmap</a>.

![density choropleth map](testdata/output/testing_taipei_crime_map2.svg?raw=true "density of some crime")  
<object id="svg1" data="testdata/output/testing_taipei_crime_map2.svg?raw=true" type="image/svg+xml" style="width: 650px; height: 480px"></object>  
link: [density choropleth map](testdata/output/testing_taipei_crime_map2.svg?raw=true)
