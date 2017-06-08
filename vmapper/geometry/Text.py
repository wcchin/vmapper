# -*- coding: utf-8 -*-

from _common_util import getsty, getanim, render

class Text:
    def __init__(self, anchor_position=[0,0], text="Text", size=24, fontfamily='Arial' text_anchor="start", layer='', color=None, opacity=None, strokecolor=None, strokewidth=None, showlabel=False, animate_times=None):
        self.xx, self.yy = anchor_position
        self.text = text

        self.fontsize = size
        self.fontfamily = fontfamily
        self.text_anchor = text_anchor
        self.opacity = opacity
        self.strokewidth = strokewidth
        self.color = color
        self.strokecolor = strokecolor
        self.animate_times = animate_times
        if len(label)>0:
            self.label = label
        else:
            self.label = index
        self.idd = index
        self.tem_dict = dict(layername=layer,showlabel=showlabel,label=self.label,idd=index)
        self.tem = 'Text.svg'

    def feature_string(self):
        sty = getsty(color=self.color, opacity=self.opacity, strokecolor=self.strokecolor, strokewidth=self.strokewidth, fontsize=self.fontsize, fontfamily=self.fontfamily)
        anim = getanim(self.idd, self.animate_times)
        self.tem_dict.update(dict(x=self.xx, y=self.yy, text_anchor=self.text_anchor, text=self.text))
        self.tem_dict.update(dict(style_str=sty, anim_str=anim))
        string_done = render(self.tem, self.tem_dict)
        return string_done
