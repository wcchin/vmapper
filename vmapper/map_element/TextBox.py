# -*- coding: utf-8 -*-
from .. import utils
from .. import geometry as geom
from . import common_function

def TextBox(text, loc, xyloc, text_anchor, size=24, fontfamily='Arial', layername='text', color=None, opacity=None, strokecolor=None, strokewidth=None, framebox=False):
    alayer = utils.Layer(layername=layername)
    if text_anchor is None:
        text_anchor = 'start'
    if xyloc is None:
        xyloc, text_anchor = common_function.get_loc(loc)

    ## TODO
    ## add rect as framebox if True (with white and transparent bg)
    alayer.addtoLayer(geom.Text(anchor_position=xyloc, text=text, size=size, fontfamily=fontfamily, text_anchor=text_anchor, layer=layername, color=color, opacity=opacity, strokecolor=strokecolor, strokewidth=strokewidth))
    return alayer
