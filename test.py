import vmapper

def test():
    paper = vmapper.Paper()
    colorby1 = {'column':"party", 'paletname':"colorbrewer", 
    'class_type':"qualitative", 'class_number':"3",'color_map':"Accent"}
    paper.addPolygon(sequence=1, source='shpfile:test_data/taiwan_county_party.shp',
        dcolor=(250,255,25),dopacity=1.0,hoveropacity=0.8,hoverswidth="500pt", 
        colorby=colorby1, labelby="CNAME"
        )#hovercolor=(0,255,0),
    #paper.addPolyline(sequence=2,source='shpfile:../GIS/jingjian3/data/merge_04d.shp')
    #paper.addPolyline(sequence=2,source='shpfile:TW_road_M2.shp')
    paper.drawToFile()
    #print paper.getsvgString()

if __name__ == '__main__':
    test()