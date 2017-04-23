# -*- coding: utf-8 -*-

from Layer import Layer
from vmapper import geometry as geom

def XY_to_points(adf, layername, draw_setting, radius, feature_sty, showlabel=False, animate_times=None):

    xs = adf[draw_setting['x']]
    ys = adf[draw_setting['y']]

    minx = min(xs)
    miny = min(ys)
    maxx = max(xs)
    maxy = max(ys)
    tb = (minx, miny, maxx, maxy)

    indexes = feature_sty['indexes']
    labels = feature_sty['labels']
    fillcolors = feature_sty['fillcolors']
    edgecolors = feature_sty['edgecolors']
    opacitys = feature_sty['opacitys']
    edgewidths = feature_sty['edgewidths']
    radiuses = feature_sty['radiuses']

    alayer = Layer(layername=layername)
    for i in range(xs):
        xx,yy = xs[i],ys[i]
        idd = indexes[i]
        lab,fc,fo,ec,ew = None,None,None,None,None
        if not(labels is None):
            lab = labels[i]
        if not(colors is None):
            fc = fillcolors[i]
        if not(opacitys is None):
            fo = opacitys[i]
        if not(edgecolors is None):
            ec = edgecolors[i]
        if not(edgewidths is None):
            ew = edgewidths[i]
        if not(radiuses is None):
            rr = radiuses[i]
        else:
            rr = radius
        center = (xx,yy)
        alayer.addtoLayer(geom.Circle(center=center, radius=rr, layer=layername, index=idd, label=lab, color=fc, opacity=fo, strokecolor=ec, strokewidth=ew, showlabel=showlabel, animate_times=animate_times))

    return alayer, tb
