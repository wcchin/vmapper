# -*- coding: utf-8 -*-

from shapely.geometry import LinearRing
from Layer import Layer
from vmapper import geometry as geom

def process_polygons(layername, geoms, indexes, labels=None, colors=None, opacitys=None, edgecolors=None, edgewidths=None, radiuses=None, showlabel=False, animate_times=None):
    alayer = Layer(layername=layername)
    gtypes = geoms.geom_type.tolist()
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
        gt = gtypes[i]
        gexs = []
        gins = []
        if gt=='Polygon':
            gex,gin = process_a_polygon(g)
            gexs = [gex]
            gins = [gin]
        elif gt=='MultiPolygon':
            mg = list(g)
            for ag in mg:
                gex,gin = process_a_polygon(ag)
                gexs.append(gex)
                gins.append(gin)
        alayer.addtoLayer(geom.MultiPolygon(exterior=gexs, interiors=gins, layer=layername, index=idd, label=lab, color=fc, opacity=fo, strokecolor=ec, strokewidth=ew, showlabel=showlabel, animate_times=animate_times))
    return alayer

def process_a_polygon(g):
    gex = list(g.exterior.coords)
    if LinearRing(gex).is_ccw:
        gex = gex[::-1]
    #geoms2.append(gex)
    gin0 = list(g.interiors)
    gin = []
    for i in gin0:
        if not i.is_ccw:
            i.coords = list(i.coords)[::-1]
        gin.append(i.coords)
    return gex,gin
