
import dxfgrabber
import numpy as np


class fromDXF():
    def __init__(self, file_loc):
        self.xmin, self.xmax, self.ymin, self.ymax = np.nan, np.nan, np.nan, np.nan
        self.dwg = dxfgrabber.readfile(file_loc)
        self.features = self.get_features()

    def get_features(self):
        features = {}
        for i in self.dwg.entities:
            dxftype = i.dxftype
            feature = None
            if dxftype not in features:
                features[dxftype] = []
            if dxftype == "LWPOLYLINE":
                lwpolyline = self._get_polyline(i)
                features[dxftype].append(lwpolyline)
            elif dxftype == "POLYLINE":
                polyline = self._get_polyline(i)
                features[dxftype].append(polyline)
            elif dxftype == "LINE":
                line = self._get_line(i)
                features[dxftype].append(line)
        return features

    def _get_polyline(self, entity):
        line=[]
        for j in entity.points:
            xx,yy = j
            self.checkbbox(xx,yy)
            line.append([xx,yy])
        return [line]

    def _get_line(self, entity):
        x1,y1,temp = entity.start
        x2,y2,temp = entity.end
        self.checkbbox(x1,y1)
        self.checkbbox(x2,y2)
        return [[[x1,y1],[x2,y2]]]

    def get_all_lines(self):
        linekeys = []
        if 'LWPOLYLINE' in self.features:
            linekeys.append('LWPOLYLINE')
        if 'POLYLINE' in self.features:
            linekeys.append('POLYLINE')
        if 'LINE' in self.features:
            linekeys.append('LINE')
        lines = []
        for key in linekeys:
            if len(lines)==0:
                lines = copy.deepcopy(self.features[key])
            else:
                lines.extend(self.features[key])
        return lines

    def bbox(self):
        return [self.xmin,self.ymin,self.xmax,self.ymax]

    def checkbbox(self,xx,yy):
        if self.xmin is np.nan:
            self.xmin=xx
        elif xx < self.xmin:
            self.xmin=xx
        if self.ymin is np.nan:
            self.ymin=yy
        elif yy < self.ymin:
            self.ymin=yy
        if self.xmax is np.nan:
            self.xmax=xx
        elif xx > self.xmax:
            self.xmax=xx
        if self.ymax is np.nan:
            self.ymax=yy
        elif yy > self.ymax:
            self.ymax=yy




def drawmap(lines, bbox, filename):
    import svg
    scene = svg.Scene('Transportation map')
    scene.updatebbox(bbox)
    layer = svg.Layer()
    layer.addtoLayer(svg.initLayer(key="04", dopacity=0.8, dscolor=(20,20,22), dswidth=20))
    for i in range(len(lines)):
        line = lines[i]
        layer.addtoLayer(svg.MultiPolylines(key=i, label=i, multiPolylines=line))
    layer.addtoLayer(svg.closeLayer())
    scene.addLayer((1, layer))

    bbox = scene.bbox
    layer = svg.Layer()
    layer.addtoLayer(svg.Rectangle((bbox[0],bbox[1]),bbox[2],bbox[3],(0,0,255), 0.1))
    scene.addLayer((0, layer))

    #print scene.getsvg()
    scene.write_svg(filename)

def test():
    file_loc = "../data/04/94193se04.dxf"
    line_entities = getlines(file_loc)
    lines = line_entities.get_lines()
    bbox = line_entities.get_bbox()
    #print bbox
    drawmap(lines, bbox, "test02.svg")

if __name__ == '__main__':
    test()