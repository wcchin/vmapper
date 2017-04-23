# -*- coding: utf-8 -*-

def fadeIn(label,t0,t1):
    begin = str(t0)+'s'
    duration = str(t1-t0)+'s'
    mainstr = '<animate id="in_%s" attributeType="CSS" attributeName="opacity" from="0" to="1" begin="%s" dur="%s" restart="never" repeatCount="1" />' % (label, begin, duration)
    return mainstr

def fadeOut(label,t0,t1):
    begin = str(t0)+'s'
    duration = str(t1-t0)+'s'
    mainstr = '<animate id="out_%s" attributeType="CSS" attributeName="opacity" from="1" to="0" begin="%s" dur="%s" restart="never" repeatCount="1" />' % (label, begin, duration)
    return mainstr

def getcolorhex(rgb):
    if rgb[0]!="#":
        return "#%x%x%x" % (rgb[0]/16,rgb[1]/16,rgb[2]/16)
    else:
        return rgb
