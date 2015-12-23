import fromShpfile
#import fromDXF

class Src():
    def __init__(self, source):
        self.source = source
        self.bbox = [0,0,0,0]
        self.fields = []
        self.recs_dict = {}
        self.shapes_dict = {}
        self.layername = ""
        self.checksource()

    def checksource(self):
        if self.source[0:7] == "postgis":
            self.getfromPostGIS()
        elif self.source[0:7] == "shpfile":
            self.getfromShpfile()
        else:
            sourcetype = self.source.split(":")[0]
            raise ValueError('source type not be implemented yet: %s' % (sourcetype))

    def getfromPostGIS(self):
        pass

    def getfromShpfile(self):
        shpdata = self.source[8:]
        filepaths = shpdata.split("/")
        filename = filepaths[len(filepaths)-1].replace(".shp", "")
        shp = fromShpfile.fromShp(shpdata)

        self.bbox = shp.bbox()
        fields = shp.fields
        for i in fields:
            self.fields.append(i[0])
        if "DeletionFlag" in self.fields:
            self.fields.remove("DeletionFlag")
        self.recs_dict = shp.recdict
        self.shapes_dict = shp.shapedict
        self.layername = filename

    def getfromDXF(self):
        pass