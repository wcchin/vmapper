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

### usage
check test.py
