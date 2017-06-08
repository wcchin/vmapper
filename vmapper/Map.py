# -*- coding: utf-8 -*-

import os
from shutil import copyfile

from Scene import Scene
import utils


class Map:
    def __init__(self, mapid=0, params={}, interactive=False):
        #default_param_dict = dict(title=None, description=None, creator=None, canvas_width="100%", canvas_height="100%", xmin=0, ymin=0, boxwidth=10, boxheight=10, hover_hightlight_items=None, bgcolor="#B3C0EF", textcolor="#000000")
        self.mapid = mapid
        self.params = params
        self.interactive = interactive
        self.layers = []
        self.styles = []
        self.bounds = self.get_bounds(params) ## (minx, miny, maxx, maxy)
        self.tot_bounds = []

    def export_to_file(self, outputfn):
        outputText = self.make_scene()
        f = open(outputfn, 'w')
        f.write(outputText.encode("utf-8"))
        print 'exported to :', outputfn

        vmapperpath = os.path.dirname(__file__)
        src = vmapperpath+'/templates/SVGPan.js'
        dst = os.path.join(os.path.dirname(outputfn),'SVGPan.js')
        if (not(os.path.exists(dst)) and self.interactive):
            copyfile(src, dst)
            print 'copied SVGPan.js file to :', dst

    def make_scene(self):
        self.scene = Scene(param_dict=self.params, interactive=self.interactive)
        for alayer in self.layers:
            self.scene.add_Layer(alayer)
        for aclasskey, asty in self.styles:
            self.scene.update_style(aclasskey , **asty)
        if self.bounds is None:
            pdict = utils.get_overall_bounds(self.tot_bounds)
            self.scene.update_param(pdict) # change the scene params
        outputText = self.scene.render()
        return outputText

    def update_param(self, pdict):
        # change the map params, should be used before calling make_scene
        self.params.update(pdict)
        self.bounds = self.get_bounds(self.params)

    def get_bounds(self, params):
        minx,miny,maxx,maxy = None,None,None,None
        if 'xmin' in params:
            minx = params['xmin']
        if 'ymin' in params:
            miny = params['ymin']
        if 'boxwidth' in params:
            boxwidth = params['boxwidth']
        if 'boxheight' in params:
            boxheight = params['boxheight']
        if ((minx is not None) and (miny is not None) and (boxwidth is not None) and (boxheight is not None)):
            bounds = (minx, miny, minx+boxwidth, miny+boxheight)
        else:
            bounds = None
        return bounds

    def add_geodataframe(self, agdf, layername, draw_setting={}, hovercolor=None,hoveropacity=None,hoverstroke=None,hoverswidth=None, color=None, opacity=None, strokecolor=None, strokewidth=None, showlabel=False, animate_times=None, radius=2.):
        # layername is classkey, classkey is layername
        feature_sty = utils.get_feature_sty(agdf, draw_setting)

        geoms = agdf.geometry
        if self.bounds is None:
            self.tot_bounds.append(geoms.total_bounds)
        
        gtype = agdf.geom_type.tolist()[0]

        # overall styles in CDATA
        asty = dict(hovercolor=hovercolor,hoveropacity=hoveropacity,hoverstroke=hoverstroke,hoverswidth=hoverswidth, color=color, opacity=opacity, strokecolor=strokecolor, strokewidth=strokewidth)

        if gtype=='Point':
            alayer = utils.process_points(layername=layername, geoms=geoms, radius=radius, showlabel=showlabel, animate_times=animate_times, **feature_sty)
        elif gtype=='LineString':
            alayer = utils.process_polylines(layername=layername, geoms=geoms, showlabel=showlabel, animate_times=animate_times, **feature_sty)
            asty['color'] = None
            asty['opacity'] = None
            asty['hovercolor'] = None
            asty['hoveropacity'] = None
        elif gtype=='Polygon' or gtype=='MultiPolygon':
            alayer = utils.process_polygons(layername=layername, geoms=geoms, showlabel=showlabel, animate_times=animate_times, **feature_sty)
        else:
            #print 'we do not support this geom_type : '+gtype
            raise ValueError('we do not support this geom_type: ', gtype)

        self.styles.append( (layername, asty) )
        self.layers.append(alayer)

    def XY_to_lines(self, adf, layername, draw_setting, hoverstroke=None,hoverswidth=None,strokecolor=None, strokewidth=None, showlabel=False, animate_times=None):
        assert 'x0' in draw_setting, 'key \'x0\'(source coords) must in draw_setting'
        assert 'y0' in draw_setting, 'key \'y0\'(source coords) must in draw_setting'
        assert 'x1' in draw_setting, 'key \'x1\'(target coords) must in draw_setting'
        assert 'y1' in draw_setting, 'key \'y1\'(target coords) must in draw_setting'

        # overall styles in CDATA
        asty = dict(hoverstroke=hoverstroke,hoverswidth=hoverswidth, strokecolor=strokecolor, strokewidth=strokewidth)
        self.styles.append( (layername, asty) )

        feature_sty = utils.get_feature_sty(adf, draw_setting)

        alayer,tb = utils.XY_to_lines(adf, layername, draw_setting, feature_sty, showlabel=showlabel, animate_times=animate_times)
        if self.bounds is None:
            self.tot_bounds.append(tb)
        self.layers.append(alayer)

    def XY_to_points(self, adf, layername, draw_setting, radius=2., hovercolor=None,hoveropacity=None,hoverstroke=None,hoverswidth=None, color=None, opacity=None, strokecolor=None, strokewidth=None, showlabel=False, animate_times=None):
        #self.dfs.append(adf)
        assert 'x' in draw_setting, 'key \'x\'(coords) must in draw_setting'
        assert 'y' in draw_setting, 'key \'y\'(coords) must in draw_setting'

        # overall styles in CDATA
        asty =  dict(hovercolor=hovercolor,hoveropacity=hoveropacity,hoverstroke=hoverstroke,hoverswidth=hoverswidth, color=color, opacity=opacity, strokecolor=strokecolor, strokewidth=strokewidth)
        self.styles.append( (layername, asty) )

        feature_sty = utils.get_feature_sty(adf, draw_setting)

        alayer, tb = utils.XY_to_points(layername, draw_setting, radius, feature_sty, showlabel=showlabel, animate_times=animate_times)

        if self.bounds is None:
            self.tot_bounds.append(tb)
        self.layers.append(alayer)
