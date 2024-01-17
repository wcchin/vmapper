# -*- coding: utf-8 -*-

from .common_util import getcolorhex
from . import fadeIO

# not rewrite yet
class Morphing_Shapes():
    def __init__(self, idd='', init_str='', begin=5, total_time=10, fading_duration=30, color=(200,200,200)):
        self.total_time = str(total_time)+'s'
        self.fadingdur = str(fading_duration)+'s'
        self.begin = str(begin)+'s'
        self.begin0 = str(begin-1)+'s'
        self.last = str(begin+total_time)+'s'
        self.fillcolor = colorstr(color)
        self.idd = idd
        self.strs = []
        self.keyTimes = []
        self.keySplines = []
        self.vertexes = []
        self.initshp = init_str

    def add_shape(self, vertexstr='', tt=0.25):
        tx = "%.3f" % tt
        self.keyTimes.append(str(tx))
        self.keySplines.append('.5,0,.5,1')
        self.vertexes.append(vertexstr)

    def strarray(self):
        vstrs = ' '.join(self.vertexes)[:-2]
        strs = ['<path d="%s" style="fill:%s; stroke:black; stroke-width:0; fill-opacity:0;">\n' % (self.initshp, self.fillcolor),
        '<animate id="in_%s" attributeType="CSS" attributeName="fill-opacity" from="0" to="1" begin="%s" dur="%s" repeatCount="1" fill="freeze" /> \n' % (self.idd, self.begin0, '1s'),
        '<animate id="morph_%s" dur="%s"  repeatCount="1" begin="in_%s.end"' % (self.idd, self.total_time, self.idd),
        'keyTimes="%s" calcMode="spline"' % ';'.join(self.keyTimes),
        'keySplines="%s"' % ';'.join(self.keySplines[:-1]),
        'attributeName="d" \n values=\n"%s"' % vstrs,'\n fill="freeze" /> \n',
        '<animate id="out_%s" attributeType="CSS" attributeName="fill-opacity" from="1" to="0" begin="morph_%s.end" dur="%s" repeatCount="1" fill="freeze" /> \n ' % (self.idd, self.idd, self.fadingdur),
        '</path>\n']
        return strs
