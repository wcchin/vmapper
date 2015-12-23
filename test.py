import mappy

def test():
    paper = mappy.Paper(filename='testingPaper03.svg')
    paper.addPolygon(sequence=1, source='shpfile:test_data/taiwan_county_party.shp')
    #paper.addPolyline(sequence=2,source='shpfile:../GIS/jingjian3/data/merge_04d.shp')
    #paper.addPolyline(sequence=2,source='shpfile:TW_road_M2.shp')
    paper.drawToFile()
    #print paper.getsvgString()

if __name__ == '__main__':
    test()