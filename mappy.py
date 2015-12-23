import datahandle.datasources as datasources
import renderer.svg as svg
import symbology.classification as classification


class Paper():
    def __init__(self, filename=None, title="default title", height="100%", width="100%", backgroundcolor="#b3c0ef", prettyprint=True):
        self.scene = svg.Scene(name=title, title=title, width=width, height=height, backgroundcolor=backgroundcolor,  prettyprint=prettyprint)
        if filename!=None:
            self.scene.setfilename(filename)
            self.filename = filename
        else:
            self.filename=title+('.html')

    def getsvgString(self):
        svgstring = self.scene.getsvg()
        return svgstring #" ".join(scene.strarray())

    def drawToFile(self):
        self.scene.write_svg(self.filename)

    def addPolygon(self, sequence=0, source=None, layername=None, colorby=None, dcolor=(255,255,255), dopacity=0.8, dscolor=(0,0,0), dswidth=200):
        if source ==None:
            raise ValueError('"source" parameter must be given')
        src = datasources.Src(source)
        if layername != None:
            Lname = layername
        else:
            Lname = src.layername
        #print Lname
        newbbox = src.bbox
        self.scene.updatebbox(newbbox)
        recs = src.recs_dict 
        fields = src.fields
        thematic = False
        colordict = None
        if colorby != None:
            try:
                colordict = classification.getColorByCol(colorby, fields, recs).getcolordict()
                thematic = True
            except:
                print "cannot create thematic map from settings"
        shps = src.shapes_dict
        layer = svg.Layer()
        layer.addtoLayer(svg.initLayer(key=Lname, dcolor=dcolor, dopacity=dopacity, dscolor=dscolor, dswidth=dswidth))
        for shp_key, shp_val in shps.iteritems():
            #clr = (float(int(random.uniform(0,255))),float(int(random.uniform(0,255))),float(int(random.uniform(0,255))))
            layer.addtoLayer(svg.MultiPolygons(key=shp_key, label=shp_key, multiPolygons=shp_val))
        layer.addtoLayer(svg.closeLayer())
        self.scene.addLayer((sequence, layer))
        print "Done adding "+source

    def addPolyline(self, sequence=0, source=None, layername=None, dopacity=0.8, dscolor=(200,0,200), dswidth=300):
        if source ==None:
            raise ValueError('"source" parameter must be given')
        src = datasources.Src(source)
        if layername != None:
            Lname = layername
        else:
            Lname = src.layername
        newbbox = src.bbox
        self.scene.updatebbox(newbbox)
        recs = src.recs_dict
        shps = src.shapes_dict
        layer = svg.Layer()
        layer.addtoLayer(svg.initLayer(key=Lname, dopacity=dopacity, dscolor=dscolor, dswidth=dswidth))
        for shp_key, shp_val in shps.iteritems():
            layer.addtoLayer(svg.MultiPolylines(key=shp_key, label=shp_key, multiPolylines=shp_val))
        layer.addtoLayer(svg.closeLayer())
        self.scene.addLayer((sequence, layer))
        print "Done adding "+source

    # artifact
    def addBBOX(self, sequence=0):
        bbox = self.scene.bbox
        layer = svg.Layer()
        layer.addtoLayer(svg.Rectangle((bbox[0]-300000,bbox[1]-300000),bbox[2]-bbox[0]+600000,bbox[3]-bbox[1]+600000,(0,0,255), 0.1))
        self.scene.addLayer((sequence, layer))

def test():
    paper = Paper(filename='testingPaper03.svg')
    paper.addPolygon(sequence=1, source='shpfile:taiwan_county_party.shp')
    #paper.addPolyline(sequence=2,source='shpfile:../GIS/jingjian3/data/merge_04d.shp')
    #paper.addPolyline(sequence=2,source='shpfile:TW_road_M2.shp')
    paper.drawToFile()
    #print paper.getsvgString()

if __name__ == '__main__':
    test()