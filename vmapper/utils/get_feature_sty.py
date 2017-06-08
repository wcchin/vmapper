# -*- coding: utf-8 -*-


def get_feature_sty(df, draw_setting):
    ## style and id and etc for each feature
    if 'idby' in draw_setting:
        ind = df[draw_setting['idby']].tolist()
    else:
<<<<<<< HEAD
        ind = df.index.tolist()
=======
        ind = agdf.index.tolist()
>>>>>>> a426d7da838d8e4ab93c4bc5ab245c7e5feb792a
    if 'labelby' in draw_setting:
        labels = df[draw_setting['labelby']].tolist()
    else:
        labels = None
    if 'colorby' in draw_setting:
<<<<<<< HEAD
        fillcolors = df[draw_setting['colorby']].tolist()
=======
        fillcolors = adf[draw_setting['colorby']].tolist()
>>>>>>> a426d7da838d8e4ab93c4bc5ab245c7e5feb792a
    else:
        fillcolors = None
    if 'edgecolorby' in draw_setting:
        edgecolors = df[draw_setting['edgecolorby']].tolist()
    else:
        edgecolors = None
    if 'opacityby' in draw_setting:
        opacitys = df[draw_setting['opacityby']].tolist()
    else:
        opacitys = None
    if 'edgewidthby' in draw_setting:
        edgewidths = df[draw_setting['edgewidthby']].tolist()
    else:
        edgewidths = None
    if 'radiusby' in draw_setting:
        radiuses = df[draw_setting['radiusby']].tolist()
    else:
        radiuses = None
    feature_sty = dict(indexes=ind, labels=labels, colors=fillcolors, opacitys=opacitys, edgecolors=edgecolors, edgewidths=edgewidths, radiuses=radiuses)
    return feature_sty
