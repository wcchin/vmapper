# -*- coding: utf-8 -*-

# this is for creating a scene, for containing the geometries and map elements

import os
import jinja2

from . import geometry

class Scene():
    def __init__(self, param_dict, interactive=False):
        self.params = param_dict
        self.layers = []
        self.map_elements = []
        self.style_items = []
        self.string_codes = []
        self.textboxs = ""
        self.interactive = interactive

    def update_param(self, adict):
        self.params.update(adict)

    def add_hover_highlight_layer(self, layername):
        if 'hover_hightlight_items' not in self.params:
            self.params['hover_hightlight_items'] = []
        self.params['hover_hightlight_items'].append('.'+layername)

    def add_Layer(self, layer):
        self.layers.append(layer)

    def add_Map_Element(self, layer):
        self.map_elements.append(layer)

    def add_strcode(self, item):
        self.string_codes.append(item)

    def update_style(self, classkey, hovercolor=None,hoveropacity=None,hoverstroke=None,hoverswidth=None, color=None, opacity=None, strokecolor=None, strokewidth=None):

        fc, fo, sc, sw = '','','',''
        if not(color is None):
            color = geometry.common_util.getcolorhex(color)
            fc = "fill:%s;\n" % (color)
        if not(opacity is None):
            fo = "fill-opacity:%s;\n" % str(opacity)
        if not(strokecolor is None):
            strokecolor = geometry.common_util.getcolorhex(strokecolor)
            sc = "stroke:%s;\n" % (strokecolor)
        if not(strokewidth is None):
            sw = "stroke-width:%s;\n" % (strokewidth)
        if not(len(fc+fo+sc+sw)==0):
            stystr = ' '.join([fc,fo,sc,sw])
            sty = '.%s {\n'%(classkey) + stystr +'\n}\n'
        else:
            sty = None
        if not(sty is None):
            self.style_items.append(sty)

        hfc, hfo, hsc, hsw = '','','',''
        if hovercolor is not None:
            hovercolor = geometry.common_util.getcolorhex(hovercolor)
            hfc = 'fill: %s;\n'%(hovercolor)
        if hoveropacity is not None:
            hfo = 'opacity: %s;\n'%str(hoveropacity)
        if hoverstroke is not None:
            hoverstroke = geometry.common_util.getcolorhex(hoverstroke)
            hsc = 'stroke:%s;\n'%(hoverstroke)
        if hoverswidth is not None:
            hsw = 'stroke-width:%s;\n'%(hoverswidth)
        if not(len(hfc+hfo+hsc+hsw)==0):
            hstystr = ' '.join([hfc, hfo, hsc, hsw])
            hsty = '.%s:hover {\n'%(classkey) + hstystr + 'pointer-events:all;\n}\n'
        else:
            hsty = None
        if not(hsty is None):
            self.style_items.append(hsty)

    def render(self):
        strs = []
        for layer in self.layers:
            layer_str = layer.get_layer_str()
            strs.append(layer_str)
        strs.extend(self.string_codes)
        draws = " ".join(strs)

        style_items = " ".join(self.style_items)

        # not implement yet, put it here (TODO)
        elements = []
        for layer in self.map_elements:
            layer_str = layer.get_layer_str()
            elements.append(layer_str)
        map_elements = " ".join(elements)

        return self.render_svg(drawing=draws, CDATA=style_items, map_elements=map_elements)

    def render_svg(self, drawing, CDATA, map_elements):
        default_param_dict = dict(title=None, description=None, creator=None, canvas_width="100%", canvas_height="100%", xmin=0, ymin=0, boxwidth=10, boxheight=10, hover_hightlight_items=None, bgcolor="#B3C0EF", textcolor="#000000")

        templateVars = self.params.copy()
        temp = { k:v for k,v in default_param_dict.items() if k not in templateVars }
        templateVars.update(temp)
        if templateVars['hover_hightlight_items'] is not None:
            templateVars['hover_hightlight_items'] = ', '.join(templateVars['hover_hightlight_items'])
        templateVars.update(dict(drawing=drawing, CDATA=CDATA, map_elements=map_elements,  interactive=self.interactive))

        vmapperpath = os.path.dirname(__file__)
        templateLoader = jinja2.FileSystemLoader( searchpath=vmapperpath+"/templates/" )
        templateEnv = jinja2.Environment( loader=templateLoader )
        TEMPLATE_FILE = "svg_template.svg"

        template = templateEnv.get_template( TEMPLATE_FILE )
        outputText = template.render( templateVars )
        return outputText
