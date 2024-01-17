# -*- coding: utf-8 -*-

from .Layer import Layer
from .. import geometry as geom

def process_points(layername, geoms, indexes, radius=2., labels=None, colors=None, opacitys=None, edgecolors=None, edgewidths=None, radiuses=None, showlabel=False, animate_times=None):
    alayer = Layer(layername=layername)
    geoms2 = geoms.tolist()
    for i in range(len(geoms2)):
        g = geoms2[i]
        idd = indexes[i]
        lab,fc,fo,ec,ew = None,None,None,None,None
        if not(labels is None):
            lab = labels[i]
        if not(colors is None):
            fc = colors[i]
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
        center = list(g.coords)[0]
        alayer.addtoLayer(geom.Circle(center=center, radius=rr, layer=layername, index=idd, label=lab, color=fc, opacity=fo, strokecolor=ec, strokewidth=ew, showlabel=showlabel, animate_times=animate_times))
    return alayer
