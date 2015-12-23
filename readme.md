mappy
=====

This is a simple python library for creating map in python, from reading spatial data source to exporting map.
Currently, only shapefile is implemented, and could only render maps to svg. 

Previously I was trying to read the codes from kartograph.py, which is currently not maintained anymore. Things I was trying to do with kartograph is to modify its postgis data source. 
But I gave up reading the codes after one full day, although it has quite complete comments within lines, it is too complicated for me.
So, I am trying to rewrite a renderer between spatial data source and svg map, that is simple to use and (hopefully) lightweight.
I also plan to write a renderer to export the maps into leaflet, maybe using folium or rewrite in similar ways. 
(The problem I found with folium is that the features are added one by one, even in one layer, that cause its layer control won't work properly.)

This library is designed to render the code string of map objects, which could be used with browser. 
The main reason I'm doing this is to create map dynamically, in web2py, a python-web-framework, which is a similar framework as flask and django. 

current status
----------
everything is still **writing**

todo list:  
----------
1.** symbology.classification**: colors partition by sequential or qualitative  
2. **symbology.transformation**: width weighting by sequential or qualitative  
3. **sourcehandle.projection**: reprojecting data from a projection to b projection  
4. **sourcehandle.frompostgis**: from postgis (or from sqlalchemy/geoalchemy)  
5. **renderer.leaflet**: render maps to leaflet  
