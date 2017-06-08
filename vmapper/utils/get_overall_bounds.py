# -*- coding: utf-8 -*-

def get_overall_bounds(tot_bounds):
    minx, miny, maxx, maxy = 999999999,999999999,-1,-1
    for alim in tot_bounds:
        x0,y0,x1,y1 = alim
        if x0<minx:
            minx = x0
        if y0<miny:
            miny = y0
        if x1>maxx:
            maxx = x1
        if y1>maxy:
            maxy = y1
    bw = maxx - minx
    bh = maxy - miny
    pdict = dict(xmin=minx, ymin=miny, boxwidth=bw, boxheight=bh)
    return pdict
