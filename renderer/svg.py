
"""
modified (extended) from code snippets: 
http://code.activestate.com/recipes/325823-draw-svg-images-in-python/

SVG.py - Construct/display SVG scenes.

The following code is a lightweight wrapper around SVG files. The metaphor
is to construct a scene, add objects to it, and then write it to a file
to display it.

This program uses ImageMagick to display the SVG files. ImageMagick also 
does a remarkable job of converting SVG files into other formats.
"""

import os
import numpy as np
display_prog = "display" # Command to execute to display images.

class Layer:
    def __init__(self):
        self.items = []

    def addtoLayer(self, item):
        self.items.append(item)
      
class Scene:
    def __init__(self,name="svg",title="testing", height=400,width=400, bbox=[np.nan, np.nan, np.nan, np.nan], color=(255,255,255), opacity=0.8, strokecolor=(0,0,0), strokewidth=0.2, backgroundcolor="#b3c0ef", prettyprint=True):
        self.name = name
        self.title = title
        self.items = []
        self.layers={}
        self.height = height
        self.width = width
        self.bbox = bbox
        self.color = colorstr(color)
        self.opacity = opacity
        self.strokecolor = colorstr(strokecolor)
        self.strokewidth = strokewidth
        self.backgroundcolor = colorstr(backgroundcolor)
        self.prettyprint = prettyprint
        return
    
    def setfilename(self, filename):
        self.name = filename

    def updatebbox(self, newbbox):
        if np.isnan(self.bbox[0]):
            self.bbox = newbbox
        else:
            xmin,ymin,xmax,ymax  = self.bbox
            xmin2,ymin2,xmax2,ymax2  = newbbox
            if xmin2<xmin:
                xmin=xmin2
            if ymin2<ymin:
                ymin=ymin2
            if xmax2>xmax:
                xmax=xmax2
            if ymax2>ymax:
                ymax=ymax
            self.bbox = [xmin,ymin,xmax,ymax]

    def addLayer(self, layertuple):
        key, layer = layertuple
        if key in self.layers:
            raise ValueError('sequence must be unique')
        else:
            self.layers.update({key: layer})

    def listinglayers(self):
        self.items = []
        seq_list = []
        for layer_seq in self.layers:
            seq_list.append(layer_seq)
        seq_list.sort()
        for key in seq_list:
            self.items.extend(self.layers[key].items)

    # artifact
    def add(self,item): self.items.append(item)

    def add_style(self):
        styles = "<style>\n"
        styles = styles + "svg {background: %s;}\n"%(self.backgroundcolor)
        styles = styles + "polyline:hover{opacity: 0.5; stroke-width:100;}\n"
        styles = styles + "polygon:hover{opacity: 0.5; stroke-width:100;}\n"
        styles = styles + "</style>\n"
        return styles

    def map_elements(self,xmin,ymin,boxheight,boxwidth):
        strs = ["<g id='header'>\n", ]
        title = Text(anchor_position=["95%","8%"],text=self.title,size=56,anchor_point="end")
        strs.extend(title.strarray())
        strs.append("</g>\n")
        me = " ".join(strs)
        return me

    def strarray(self):
        #print self.bbox
        self.listinglayers()
        xmin,ymin,xmax,ymax  = self.bbox
        boxwidth = xmax-xmin
        boxheight = ymax-ymin
        styles = self.add_style()
        map_elements = self.map_elements(xmin,ymin,boxheight,boxwidth)
        var = ["<?xml version=\"1.0\"?>\n",
               "<svg version=\"1.2\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink= \"http://www.w3.org/1999/xlink\" xmlns:ev=\"http://www.w3.org/2001/xml-events\"  baseProfile=\"tiny\" \n", 
               "width=\"%s\" height=\"%s\">\n" % (self.width,self.height),
               map_elements,
               "<svg width=\"%s\" height=\"%s\" viewBox=\"%r %r %r %r\" preserveAspectRatio=\"xMidYMid meet\" viewport-fill=\"%s\">\n" % ("100%","100%", xmin, ymin, boxwidth, boxheight, self.backgroundcolor),
               styles,
               "<script xlink:href=\"SVGPan.js\" />\n<g id=\"viewport\">\n",
               "<g transform=\"translate(%r %r) scale(1,-1)\">\n" %(0, 2*ymin+boxheight),#%(-xmin, ymin+boxheight),
               "<g style=\"fill: %s; fill-opacity:%s; " %(self.color, self.opacity),
               "stroke:%s; stroke-width:%s;\">\n"%(self.strokecolor, self.strokewidth)]
        for item in self.items: var += item.strarray()
        var += ["</g>\n</g>\n</g>\n</svg>\n</svg>\n"]
        return var

    def write_svg(self,filename=None):
        if filename:
            self.svgname = filename
        else:
            self.svgname = self.name + ".html"
        file = open(self.svgname,'w')
        file.writelines(self.getsvg())
        file.close()
        return

    def display(self,prog=display_prog):
        os.system("%s %s" % (prog,self.svgname))
        return        

    def getsvg(self):
        strings="".join(self.strarray())
        if self.prettyprint:
            return strings
        else:
            return strings.replace("  "," ").replace("\n", " ")
        
class initLayer:
    def __init__(self, key='layername', title='Layer label', dcolor=None, dopacity=0.8, dscolor=(0,0,0), dswidth=0.6, dsarray=None):
        self.key = key
        if dcolor != None:
            self.dcolor = colorstr(dcolor)
        else:
            self.dcolor = "none"
        self.dopacity = dopacity
        self.dscolor = colorstr(dscolor)
        self.dswidth = dswidth
        self.dsarray = dsarray
        self.title = title
        return

    def strarray(self):
        string = '<g id="%s" style=\"fill: %s; fill-opacity:%s; stroke:%s; stroke-width:%s;' % (self.key, self.dcolor, self.dopacity, self.dscolor, self.dswidth)
        if self.dsarray != None:
            string = string + 'stroke-dasharray: %s; ' % (self.dsarray)
        string = string + '\">\n'
        string = string + '<title> %s </title>\n' % (self.title)
        return [string]

class closeLayer:
    def __init__(self):
        #pass
        return

    def strarray(self):
        string = "</g>\n"
        return [string]

class Line:
    def __init__(self,start,end):
        self.start = start #xy tuple
        self.end = end     #xy tuple
        return

    def strarray(self):
        return ["  <line x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\" />\n" %\
                (self.start[0],self.start[1],self.end[0],self.end[1])]


class MultiPolygons:
    def __init__(self, key=0, label='label', multiPolygons=None, color=None, opacity=None):
        self.key = key
        if label != 'label':
            self.label = str(label)
        else:
            self.label = str(key)
        self.multiPolygons = multiPolygons # list of xy tuple
        if color!=None:
            self.color = colorstr(color)
        else:
            self.color = None
        self.opacity = opacity
        return

    def strarray(self):
        string = '<g id="%s" style=" ' %(self.key)
        if self.color != None:
            string = string + 'fill: %s; ' % (self.color)
        if self.opacity != None:
            string = string + 'fill-opacity: %s; ' % (self.opacity)
        string = string + '">'+'<title>'+self.label+'</title>'
        for polygon in self.multiPolygons:
            string=string+'<polygon points="'
            for point in polygon:
                string = string + str(point[0])+ ","+str(point[1]) + "  "
            string = string+'" />' 
        string = string+'</g>\n' 
        #print string
        return [string]

class MultiPolylines:
    def __init__(self, key=0, label='label', multiPolylines=None, strokecolor=None, strokewidth=None):
        self.key = key
        if label != 'label':
            self.label = str(label)
        else:
            self.label = str(key)
        self.multiPolylines = multiPolylines # list of xy tuple
        if strokecolor != None:
            self.strokecolor = colorstr(strokecolor)
        else:
            self.strokecolor = None
        self.strokewidth = strokewidth
        return

    def strarray(self):
        string = '<g id="%s" style="' %(self.key)
        if self.strokecolor != None:
            string = string + 'stroke: %s; ' % (self.strokecolor)
        if self.strokewidth != None:
            string = string + 'stroke-width: %s; ' % (self.strokewidth)
        string = string + '">'+'<title>'+self.label+'</title>'
        if string[-3:-1] == '\"\"':
            string = string[0:-10]+">"
        for polyline in self.multiPolylines:
            string=string+'<polyline points="'
            for point in polyline:
                string = string + str(point[0])+ ","+str(point[1]) + "  "
            string = string[:-2]+'" />' 
        string = string+'</g>\n' 
        #print string
        return [string]

class Circle:
    def __init__(self,center,radius,color):
        self.center = center #xy tuple
        self.radius = radius #xy tuple
        self.color = color   #rgb tuple in range(0,256)
        return

    def strarray(self):
        return ["  <circle cx=\"%d\" cy=\"%d\" r=\"%d\"" %\
                (self.center[0],self.center[1],self.radius),
                "    style=\"fill:%s;\"  />\n" % colorstr(self.color)]

class Rectangle:
    def __init__(self,origin,width,height,color,opacity):
        self.origin = origin
        self.height = height
        self.width = width
        self.color = color
        self.opacity = opacity
        return

    def strarray(self):
        return ["  <rect x=\"%s\" y=\"%s\" height=\"%s\"" %\
                (self.origin[0],self.origin[1],self.height),
                " width=\"%s\" style=\"fill:%s; fill-opacity:%s\" />\n" %\
                (self.width,colorstr(self.color),self.opacity)]

class Text:
    def __init__(self,anchor_position=[0,0],text="Text",size=24,anchor_point="start"):
        self.origin = anchor_position
        self.text = text
        self.size = size
        self.anchor_point = anchor_point
        return

    def strarray(self):
        return ["  <text x=\"%s\" y=\"%s\" font-size=\"%d\" text-anchor=\"%s\">\n" %\
                (self.origin[0],self.origin[1],self.size, self.anchor_point),
                "   %s\n" % self.text,
                "  </text>\n"]
        
    
def colorstr(rgb): 
    if rgb[0]!="#":
        return "#%x%x%x" % (rgb[0]/16,rgb[1]/16,rgb[2]/16)
    else:
        return rgb

def test():
    scene = Scene('test')
    scene.add(Rectangle((100,100),200,200,(0,255,255),0.8))
    scene.add(Line((200,200),(200,300)))
    scene.add(Line((200,200),(300,200)))
    scene.add(Line((200,200),(100,200)))
    scene.add(Line((200,200),(200,100)))
    scene.add(Circle((200,200),30,(0,0,255)))
    scene.add(Circle((200,300),30,(0,255,0)))
    scene.add(Circle((300,200),30,(255,0,0)))
    scene.add(Circle((100,200),30,(255,255,0)))
    scene.add(Circle((200,100),30,(255,0,255)))
    scene.add(MultiPolygons(multiPolygons=[[[50,50], [75,50],[50,75]]], color=(0,0,255)))
    scene.add(initLayer(key='layername', dopacity=0.8, dscolor=(255,0,0), dswidth=2.0))
    scene.add(MultiPolylines(multiPolylines=[[[50,50], [135,155], [175,50],[150,75]]]))
    scene.add(closeLayer())
    scene.add(Text((50,50),"Testing SVG"))
    #scene.write_svg()
    #scene.display()
    return " ".join(scene.strarray())

if __name__ == '__main__': 
    print test()
