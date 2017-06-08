# -*- coding: utf-8 -*-

import numpy as np
from common_util import getcolorhex
#import fadeIO


## not rewrite yet
class Animated_Line:
    def __init__(self, idd='', start=(), end=(), t0=1, t1=5):
        self.start = start #xy tuple
        self.end = end     #xy tuple
        x0,y0 = start
        x1,y1 = end
        dur = t1-t0+1
        begin = t0-1
        self.strs = [' <line x1="%d" y1="%d" x2="%d" y2="%d"  style="stroke:rgb(180,0,0);stroke-width:20">\n' %                 (x0,y0,x0,y0)]
        dx = (x1-x0)/float(dur)
        dy = (y1-y0)/float(dur)
        beg = 0
        for i in range(int(np.ceil(dur-1))):
            j=i+1
            xnew = x0 + j*dx
            ynew = y0 + j*dy
            beg = j+begin
            self.strs.append('<set attributeName="x2" to="%d" begin="%s" /> ' % (xnew, str(beg)+'s'))
            self.strs.append('<set attributeName="y2" to="%d" begin="%s" /> \n' % (ynew, str(beg)+'s'))
        self.strs.extend(['<animate id="fadeout_%s" attributeType="CSS" attributeName="opacity" from="1" to="0" begin="%s" dur="%s" restart="never" fill="freeze"/> \n' % (idd, beg, 1),
        '</line>\n'])

    def feature_string(self):
        return self.strs
