# -*- coding: utf-8 -*-

import os
import jinja2

import _fadeIO


def render(TEMPLATE_FILE, templateVars):
    vmapperpath = os.path.dirname(__file__)
    templateLoader = jinja2.FileSystemLoader( searchpath=vmapperpath+"/templates/" )
    templateEnv = jinja2.Environment( loader=templateLoader )
    template = templateEnv.get_template( TEMPLATE_FILE )
    outputText = template.render( templateVars )
    return outputText

def getcolorhex(rgb):
    if rgb=='transparent':
        return rgb
    elif rgb[0]!="#":
        return "#%x%x%x" % (rgb[0]/16,rgb[1]/16,rgb[2]/16)
    else:
        return rgb

def getsty(color=None, opacity=None, strokecolor=None, strokewidth=None, fontsize=None, fontfamily=None):
    if color=='none':
        color = color
    elif color!=None:
        color = getcolorhex(color)
    if strokecolor!=None:
        strokecolor = getcolorhex(strokecolor)

    fc,fo,sc,sw,fs,fm = '','','','','',''
    if not(color is None):
        fc = "fill:%s;" % (color)
    if not(opacity is None):
        fo = "fill-opacity:%s;" % (opacity)
    if not(strokecolor is None):
        sc = "stroke:%s;" % (strokecolor)
    if not(strokewidth is None):
        sw = "stroke-width:%s;" % (strokewidth)
    if not(fontsize is None):
        fs = "font-size:%spx;" % (self.fontsize)
    if not(fontfamily is None):
        fm = "font-family:%spx;" % (self.fontfamily)

    if not(len(fs+fm+fc+fo+sc+sw)==0):
        stystr = ' '.join([fs,fm,fc,fo,sc,sw])
        sty = 'style="%s" ' % stystr
    else:
        sty = ' '
    return sty

def getanim(label, animate_times):
    if not(animate_times is None):
        t0,t1,t2,t3 = None,None,None,None
        if 't0' in animate_times:
            t0 = animate_times['t0']
        if 't1' in animate_times:
            t1 = animate_times['t1']
        if 't2' in animate_times:
            t2 = animate_times['t2']
        if 't3' in animate_times:
            t3 = animate_times['t3']
        fadein = not(t0 is None) and not(t1 is None)
        fadeOut = not(t2 is None) and not(t3 is None)
        in_str, out_str = '',''
        if fadein:
            in_str = fadeIO.fadeIn(label,t0,t1)
        if fadeout:
            out_str = fadeIO.fadeOut(label,t2,t3)
        if len(in_str+out_str)>0:
            anim = '\n'+'\n'.join([in_str,out_str])+'\n'
        else:
            anim = ''
    else:
        anim = ''
    return anim
