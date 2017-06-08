# -*- coding: utf-8 -*-

from _common_util import getsty, getanim, render

class Rectangle:
    def __init__(self, origin, width, height,index=0, layer='', label='', color=None, opacity=None, strokecolor=None, strokewidth=None, showlabel=False, animate_times=None):
        self.xx, self.yy = origin
        self.height = height
        self.width = width

        self.opacity = opacity
        self.strokewidth = strokewidth
        self.color = color
        self.strokecolor = strokecolor
        if len(label)>0:
            self.label = label
        else:
            self.label = index
        self.idd = index
        self.tem_dict = dict(layername=layer,showlabel=showlabel,label=self.label,idd=index)
        self.tem = 'Rectangle.svg'

    def feature_string(self):
        sty = getsty(color=self.color, opacity=self.opacity, strokecolor=self.strokecolor, strokewidth=self.strokewidth)
        anim = getanim(self.idd, self.animate_times)
        self.tem_dict.update(dict(x=self.xx, y=self.yy, h=self.height, w=self.width))
        self.tem_dict.update(dict(style_str=sty, anim_str=anim))
        string_done = render(self.tem, self.tem_dict)
        return string_done
