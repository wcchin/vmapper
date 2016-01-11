
#import brewer2mpl
#import palettable as palet
import importlib
import numpy as np

class getColorByCol():
    def __init__(self, colorby, fieldlist, recdict):
        self.colorby = colorby

        self.colordict = {}
        col = colorby['column']
        try:
            ind = fieldlist.index(col)
        except:
            raise ValueError('cannot locate column %s from shpfile.' % (col))

        vallist = []
        colrec = {}
        for key, val in recdict.iteritems():
            #print key
            cval = val[ind]
            #print cval
            colrec[key] = cval
            vallist.append(cval)
        self.setlist = list(set(vallist))
        #print "haha"

        colorlist = self.get_colors()
        #print colorlist
        if 'class_type' in colorby:
            class_type = colorby['class_type']
        else:
            class_type = 'qualitative'

        if class_type == 'sequential':
            class_method = 'equal_interval'
            if 'class_method' in colorby:
                class_method = colorby['class_method']
            class_number = len(colorlist)
            ncuts = numeric_cuts(vallist, class_method, class_number)
            self.cuts = ncuts.cuts
            pass
        elif class_type == 'qualitative':
            for key, val in colrec.iteritems():
                self.colordict[key] = colorlist[self.setlist.index(val)]

    def getcolordict(self):
        return self.colordict


    def get_colors(self):
        colorby = self.colorby
        if 'class_type' in colorby:
            class_type = colorby['class_type']
        else:
            class_type = 'qualitative'

        color_map = 'Margot2_4'
        if 'color_map' in colorby:
            color_map = colorby['color_map']

        paletname = 'colorbrewer'
        if 'paletname' in colorby:
            paletname = colorby['paletname']

        if paletname == 'colorbrewer':
            if class_type == "qualitative":
                class_number = len(self.setlist)
            else:
                class_number = 5
                if 'class_number' in colorby:
                    class_number = colorby['class_number']

            colorlist = self.use_colorbrewer(class_type, color_map, class_number)

        elif paletname == "cubehelix":
            if class_type == "qualitative":
                class_number = len(self.setlist)
            else:
                class_number = 5
                if 'class_number' in colorby:
                    class_number = colorby['class_number']
            if class_number > 16:
                color_map = "manual"
            else:
                color_map = 'manual'
                color_map = colorby['color_map']
            #print color_map
            colorlist = self.use_cubehelix(color_map, class_number)

        elif paletname == "use_wesanderson":
            colorlist = self.use_use_wesanderson(color_map)
        return colorlist

    def use_colorbrewer(self, class_type, color_map, class_number):
        no = int(float(class_number))
        if no < 3:
            cn = 3
        elif no > 11:
            cn = 11
        else:
            cn = no
        importc = "palettable.colorbrewer" +"."+ class_type
        pc = importlib.import_module(importc)
        bmap = getattr(pc, color_map + "_"+str(cn))
        if no <= 11:
            colorlist = bmap.hex_colors
        else:
            from colormap import rgb2hex
            cmap = bmap.get_mpl_colormap(N=no, gamma=2.0)
            colorlist = []
            for c in cmap:
                rr,gg,bb,aaa = c
                colr = rgb2hex(rr*255,gg*255,bb*255)
                colorlist.append(colr)
        return colorlist

    def use_cubehelix(self, color_map, class_number=None):
        if color_map != "manual":
            importc = "palettable.cubehelix"
            pc = importlib.import_module(importc)
            bmap = getattr(pc, color_map)
        else:
            importc = "palettable.cubehelix"
            pc = getattr(importlib.import_module(importc), "Cubehelix")
            bmap = pc.make(n=class_number)
        colorlist = bmap.hex_colors
        return colorlist

    def use_wesanderson(self, color_map):
        importc = "palettable.cubehelix"
        pc = importlib.import_module(importc)
        bmap = getattr(pc, color_map)
        colorlist = bmap.hex_colors
        return colorlist


class numeric_cuts():
    def __init__(self, val_list, class_method, class_number):
        self.cuts = []
        #val_list.sort()
        self.val_list = val_list
        #self.setlist = list(set(val_list))
        self.class_number = class_number
        self.start = min(val_list)
        self.end = max(val_list)

        if class_method == "equal_interval":
            self.cuts = self.equal_interval()
        elif class_method == "quantile":
            self.cuts = self.quantile()
        elif class_method == "standard_deviation":
            self.cuts = self.standard_deviation()

    def equal_interval(self):
        cuts = np.linspace(self.start, self.end, num=self.class_number, endpoint=False).tolist()
        cuts.append(self.end)
        return cuts

    def quantile(self):
        q_percent = 1.0/self.class_number * 100.0
        cut = np.percentile(self.val_list, q_percent)
        cuts = [i*cut + self.start for i in range(self.class_number)]
        cuts.append(self.end)
        return cuts

    def standard_deviation(self):
        pass

def test():
    pass

if __name__ == '__main__':
    test()