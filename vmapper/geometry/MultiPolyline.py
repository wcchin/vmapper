# -*- coding: utf-8 -*-

from ._common_util import getsty, getanim, render

class MultiPolyline:
    def __init__(self, vertexes, index=0, layer='', label='', strokecolor=None, strokewidth=None, showlabel=False, animate_times=None):
        self.vertexes = vertexes

        self.strokewidth = strokewidth
        self.strokecolor = strokecolor
        self.animate_times = animate_times
        if len(label)>0:
            self.label = label
        else:
            self.label = index
        self.idd = index
        self.tem_dict = dict(layername=layer,showlabel=showlabel,label=self.label,idd=index)
        self.tem = 'MultiPolyline.svg'

    def feature_string(self):
        mainstr = get_pathstring(self.vertexes)  # get_arcstring(self.vertexes)
        sty = getsty(strokecolor=self.strokecolor, strokewidth=self.strokewidth, color='none')
        anim = getanim(self.idd, self.animate_times)
        self.tem_dict.update(dict(geom_str=mainstr, style_str=sty, anim_str=anim))
        string_done = render(self.tem, self.tem_dict)
        return string_done
"""
def get_arcstring(vertexlist):
    if len(vertexlist)>1:
        string = ''
        for a in vertexlist:
            x = a[0]
            y = a[1]
            string = string + "{:.6f},{:.6f} ".format(x, y)
            #  "%.6f"%(x)+","+"%.6f"%(y) + "  "
        return string
    else:
        print( 'vertexlist is too short (<2), returning None')
        return None
"""

def get_pathstring(vertexlist):
    if len(vertexlist)>1:
        string = 'M '
        for x, y in vertexlist:
            string = string + "{:.6f} {:.6f} L ".format(x, y)
            #"%.6f"%(x)+","+"%.6f"%(y)+" L "
        string = string[:-2]#+'Z '
        return string
    else:
        print('vertexlist is too short (<2), returning None')
        return None