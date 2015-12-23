import os
import shapefile
import numpy as np
#import pandas as pd

class fromShp(object):
    def __init__(self, inputshppath):
        sf = self.openshpfile(inputshppath)
        self.shapes = sf.shapes()
        self.fields = sf.fields
        self.records = sf.records()
        self.shapetype = self.shapes[0].shapeType
        col_list = [self.fields[c][0] for c in range(len(self.fields))]
        col_list.remove(col_list[0])
        self.recdict = self.datareading()
        self.shapedict = self.getshapedict()
        self.locdict = {}
        #self.bb = self.bbox()
        #self.colsets = self.colsetting()
        #self.datareading()

    def openshpfile(self,inputshppath):
        currentpath = os.getcwd()
        abspath = os.path.abspath(inputshppath)
        inputpath = os.path.dirname(abspath)
        inputshp = os.path.basename(inputshppath)
        os.chdir(inputpath)
        #print os.getcwd()
        sf = shapefile.Reader(inputshp)
        os.chdir(currentpath)
        return sf

    def fieldList(self):
        number_long_fieldlist = []
        for i in range(len(self.fields)):
            if self.fields[i][1] in ("N", "I", "F", "O"):
                number_long_fieldlist.append(self.fields[i][0])
        return number_long_fieldlist
    
    def possibleLocList(self):
        possibleList = []
        for i in range(len(self.fields)):
            if self.fields[i][1] in ("C", "N", "I", "F", "O"):
                possibleList.append(self.fields[i][0])
        if "DeletionFlag" in possibleList:
            possibleList.remove("DeletionFlag")
        return possibleList
    
    def bbox(self):
        x1 = np.NaN
        x2 = np.NaN
        y1 = np.NaN
        y2 = np.NaN
        
        all_shapes = self.shapes
        for i in range(len(all_shapes)):
            thisbbox = all_shapes[i].bbox
            if np.isnan(x1):
                x1 = thisbbox[0]
                y1 = thisbbox[1]
                x2 = thisbbox[2]
                y2 = thisbbox[3]
            else:
                if thisbbox[0] < x1:
                    x1 = thisbbox[0]
                if thisbbox[1] < y1:
                    y1 = thisbbox[1]
                if thisbbox[2] > x2:
                    x2 = thisbbox[2]
                if thisbbox[3] > y2:
                    y2 = thisbbox[3]
            
        xlen = x2 - x1
        ylen = y2 - y1
        """
        if xlen > ylen:
            lenchange = (xlen - ylen) / 2
            y1 = y1 - lenchange
            y2 = y2 + lenchange
        else:
            lenchange = (ylen - xlen) / 2
            x1 = x1 - lenchange
            x2 = x2 + lenchange
        """
        return [x1, y1, x2, y2]

    def datareading(self):
        recdict = {}
        key_now = 0
        for record in self.records:
            recdict.update({key_now: record})
            """
            data = np.array(shape.points)
            if len(shape.parts) == 1:
                segs = [data,]
            else:
                segs = []
                for i in range(1,len(shape.parts)):
                    index = shape.parts[i-1]
                    index2 = shape.parts[i]
                    segs.append(data[index:index2])
                segs.append(data[index2:])
            segs_now = {key_now: segs}
            self.segdict.update(segs_now)
            """
            key_now = key_now + 1
        return recdict

    def getshapedict(self):
        shapetype = self.shapes[0].shapeType
        shapedict = {}
        if shapetype == 1:
            shapedict = self.getPoint()
        elif shapetype == 3:
            shapedict = self.getMultiPolyline()
        elif shapetype == 5:
            shapedict = self.getMultiPolygon()
        else:
            print "shapefile shapeType not implement yet:", str(shapetype)
        return shapedict

    def getPoint(self):
        return

    def getMultiPolyline(self):
        multiPolylines = {}
        key_now = 0
        for shape in self.shapes:
            data = np.array(shape.points)
            if len(shape.parts) == 1:
                segs = [data,]
            else:
                segs = []
                for i in range(1,len(shape.parts)):
                    index = shape.parts[i-1]
                    index2 = shape.parts[i]
                    segs.append(data[index:index2])
                segs.append(data[index2:])
            segs_now = {key_now: segs}
            multiPolylines.update(segs_now)
            key_now = key_now + 1
        return multiPolylines
        
    def getMultiPolygon(self):
        multiPolygons = {}
        key_now = 0
        for shape in self.shapes:
            data = np.array(shape.points)
            if len(shape.parts) == 1:
                segs = [data,]
            else:
                segs = []
                for i in range(1,len(shape.parts)):
                    index = shape.parts[i-1]
                    index2 = shape.parts[i]
                    segs.append(data[index:index2])
                segs.append(data[index2:])
            segs_now = {key_now: segs}
            multiPolygons.update(segs_now)
            key_now = key_now + 1
        return multiPolygons

def test():
    import random
    #shp = fromShp('taipei_bound_84.shp')
    shp = fromShp('taiwan_county_party.shp')
    #shp = fromShp('ne_50m_admin_0_countries.shp')
    bbox = shp.bbox()
    recs = shp.recdict
    segs = shp.shapedict
    scene = svg.Scene('test', title="testing", width=800, height=600, bbox=bbox, prettyprint=False)
    scene.add(svg.Rectangle((bbox[0],bbox[1]),bbox[2],bbox[3],(0,0,255), 0.2))
    scene.add(svg.initLayer(key='layername', dcolor=(255,255,255), dopacity=0.8, dscolor=(0,0,0), dswidth=0.6))
    for seg_key, seg_val in segs.iteritems():
        clr = (float(int(random.uniform(0,255))),float(int(random.uniform(0,255))),float(int(random.uniform(0,255))))
        scene.add(svg.MultiPolygons(key=seg_key, label=seg_key, multiPolygons=seg_val, color=clr, opacity=0.8))
    scene.add(svg.closeLayer())
    scene.write_svg("test6.html")
    #scene.display()
    svgstring = scene.getsvg()
    return svgstring #" ".join(scene.strarray())

def test2():
    #shp = fromShp('TW_RAIL.shp')
    shp = fromShp('TW_road_M2.shp')
    #shp = fromShp('TW_RAIL.shp')
    bbox = shp.bbox()
    recs = shp.recdict
    segs = shp.shapedict
    scene = svg.Scene('test', title="testing", width=800, height=600, bbox=bbox, prettyprint=True)
    scene.add(svg.Rectangle((bbox[0],bbox[1]),bbox[2],bbox[3],(0,255,255), 0.1))
    scene.add(svg.initLayer(key='layername', dopacity=1.0, dscolor=(255,255,255), dswidth=500))
    for seg_key, seg_val in segs.iteritems():
        #clr = (float(int(random.uniform(0,255))),float(int(random.uniform(0,255))),float(int(random.uniform(0,255))))
        #print seg_val
        scene.add(svg.MultiPolylines(key=seg_key, label=seg_key, multiPolylines=seg_val))
    scene.add(svg.closeLayer())
    scene.write_svg("test7.html")
    #scene.display()
    svgstring = scene.getsvg()
    return svgstring #" ".join(scene.strarray())



def test3():
    #shp = fromShp('taipei_bound_84.shp')
    shp = fromShp('taiwan_county_party.shp')
    #shp = fromShp('ne_50m_admin_0_countries.shp')
    bbox = shp.bbox()
    recs = shp.recdict
    segs = shp.shapedict
    scene = svg.Scene('test', title="testing", width=800, height=600, bbox=bbox, prettyprint=False)
    scene.add(svg.Rectangle((bbox[0],bbox[1]),bbox[2],bbox[3],(0,0,255), 0.2))
    scene.add(svg.initLayer(key='layername', dopacity=0.8, dscolor=(0,255,0), dswidth=15))
    #scene.add(svg.initLayer(key='layername', dopacity=1.0, dscolor=(0,255,0), dswidth=3))
    for seg_key, seg_val in segs.iteritems():
        #clr = (float(int(random.uniform(0,255))),float(int(random.uniform(0,255))),float(int(random.uniform(0,255))))
        scene.add(svg.MultiPolylines(key=seg_key, label=seg_key, multiPolylines=seg_val))
    scene.add(svg.closeLayer())
    scene.write_svg("test6.html")
    #scene.display()
    svgstring = scene.getsvg()
    return svgstring #" ".join(scene.strarray())


if __name__ == '__main__':
    import svg
    #test = test2()
    #print test
    shp = fromShp('taiwan_county_party.shp')
    print shp.fields
    print shp.recdict[0]