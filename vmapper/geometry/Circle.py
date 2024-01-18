# -*- coding: utf-8 -*-

from ._common_util import getsty, getanim, render

class Circle:
    def __init__(self, center, radius, index=0, layer='', label='', color=None, opacity=None, strokecolor=None, strokewidth=None, showlabel=False, animate_times=None, visibility='visible'):
        self.xx, self.yy = center #xy tuple
        self.radius = radius #xy tuple

        self.opacity = opacity
        self.strokewidth = strokewidth
        self.color = color
        self.strokecolor = strokecolor
        self.visibility = visibility
        self.animate_times = animate_times
        if len(label)>0:
            self.label = label
        else:
            self.label = index
        self.idd = index
        self.tem_dict = dict(layername=layer,showlabel=showlabel,label=self.label,idd=index)
        self.tem = 'Circle.svg'

    def feature_string(self):
        sty = getsty(color=self.color, opacity=self.opacity, strokecolor=self.strokecolor, strokewidth=self.strokewidth, visibility=self.visibility)
        anim = getanim(self.idd, self.animate_times)
        self.tem_dict.update(dict(cx=self.xx, cy=self.yy, r=self.radius))
        self.tem_dict.update(dict(style_str=sty, anim_str=anim))
        string_done = render(self.tem, self.tem_dict)
        return string_done
