# -*- coding: utf-8 -*-
from .. import utils
#from vmapper import geometry as geom
from .. import geometry as geom
from . import common_function

def ColorLegend(color_tuple, loc, xyloc, text_anchor, size=12, fontfamily='Arial', layername='Legend', color=None, opacity=None, strokecolor=None, strokewidth=None, framebox=False, legend_title=True):
    alayer = utils.Layer(layername=layername)
    if text_anchor is None:
        text_anchor = 'start'
    if xyloc is None:
        xyloc, text_anchor = common_function.get_loc2(loc)

    x,y = xyloc
    xx = int(x[:-1])
    yy = int(y[:-1])

    if legend_title:
        ap = [str(xx)+'%',str(yy)+'%']
        alayer.addtoLayer(geom.Text(anchor_position=ap, text=layername, size=size+4, fontfamily=fontfamily, text_anchor=text_anchor, layer=layername, color=color, opacity=opacity, strokecolor=strokecolor, strokewidth=strokewidth))
        #xx+=size/3
        yy+=size/3

    for ind,lab,col in color_tuple:
        ap1 = [str(xx)+'%',str(yy)+'%']
        ap2 = [str(xx+1.2)+'%',str(yy+0.7)+'%']
        alayer.addtoLayer(geom.Rectangle(ap1, 10, 8 , index=ind, color=col, label=lab, opacity=opacity, strokewidth=strokewidth, strokecolor=strokecolor))
        alayer.addtoLayer(geom.Text(anchor_position=ap2, text=lab, size=size, fontfamily=fontfamily, text_anchor=text_anchor, layer=layername, color=color, opacity=opacity, strokecolor=strokecolor, strokewidth=0.))
        yy+=size/3
    return alayer
