# -*- coding: utf-8 -*-

from Layer import Layer
from vmapper import geometry as geom

def process_polylines(layername, geoms, indexes, labels=None, colors=None, opacitys=None, edgecolors=None, edgewidths=None, radiuses=None, showlabel=False, animate_times=None):
    alayer = Layer(layername=layername)
    geoms2 = geoms.tolist()
    for i in range(len(geoms2)):
        g = geoms2[i]
        idd = indexes[i]
        lab,fc,fo,ec,ew = None,None,None,None,None
        if not(labels is None):
            lab = labels[i]
        if not(edgecolors is None):
            ec = edgecolors[i]
        if not(edgewidths is None):
            ew = edgewidths[i]
        line = list(g.coords)
        alayer.addtoLayer(geom.MultiPolyline(vertexes=line, layer=layername, index=idd, label=lab, strokecolor=ec, strokewidth=ew, showlabel=showlabel, animate_times=animate_times))
    return alayer
