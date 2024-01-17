# -*- coding: utf-8 -*-

from .Layer import Layer
from .. import geometry as geom

def XY_to_lines(adf, layername, draw_setting, feature_sty, showlabel=False, animate_times=None):

    x0s = adf[draw_setting['x0']]
    y0s = adf[draw_setting['y0']]
    x1s = adf[draw_setting['x1']]
    y1s = adf[draw_setting['y1']]

    minx = min(min(x0s),min(x1s))
    miny = min(min(y0s),min(y1s))
    maxx = max(max(x1s),max(x0s))
    maxy = max(max(y1s),max(y0s))
    tb = (minx, miny, maxx, maxy)

    indexes = feature_sty['indexes']
    labels = feature_sty['labels']
    edgecolors = feature_sty['edgecolors']
    edgewidths = feature_sty['edgewidths']

    alayer = Layer(layername=layername)
    for i in range(x0s):
        x0,y0,x1,y1 = x0s[i],y0s[i],x1s[i],y1s[i]
        idd = indexes[i]
        lab,ec,ew = None,None,None,None,None
        if not(labels is None):
            lab = labels[i]
        if not(edgecolors is None):
            ec = edgecolors[i]
        if not(edgewidths is None):
            ew = edgewidths[i]
        alayer.addtoLayer(geom.Line(start=(x0,y0), end=(x1,y1), layer=layername, index=idd, label=lab, strokecolor=ec, strokewidth=ew, showlabel=showlabel, animate_times=animate_times))

    return alayer, tb
