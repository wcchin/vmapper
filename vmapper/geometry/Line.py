# -*- coding: utf-8 -*-

from ._common_util import getsty, getanim, render

class Line:
    def __init__(self, start, end, index=0, layer='', label='', strokecolor=None, strokewidth=None, showlabel=False, animate_times=None):
        self.x0, self.y0 = start #xy tuple
        self.x1, self.y1 = end   #xy tuple

        self.strokewidth = strokewidth
        self.strokecolor = strokecolor
        if len(label)>0:
            self.label = label
        else:
            self.label = index
        self.idd = index
        self.tem_dict = dict(layername=layer,showlabel=showlabel,label=self.label,idd=index)
        self.tem = 'Line.svg'

    def feature_string(self):
        sty = getsty(strokecolor=self.strokecolor, strokewidth=self.strokewidth)
        anim = getanim(self.idd, self.animate_times)
        self.tem_dict.update(dict(x0=self.x0, y0=self.y0, x1=self.x1, y1=self.y1))
        self.tem_dict.update(dict(style_str=sty, anim_str=anim))
        string_done = render(self.tem, self.tem_dict)
        return string_done
