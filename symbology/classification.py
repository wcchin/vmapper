
import brewer2mpl
import numpy as np

class getColorByCol():
    def __init__(self, colorby, fieldlist, recdict):
        self.colordict = {}
        col = colorby['column']
        try:
            ind = fields.index(col)
        except:
            raise ValueError('cannot locate column %s from shpfile.' % (col))
        class_method = 'equal_interval'
        class_number = 5
        color_map = 'YlGnBu'
        if 'class_method' in colorby:
            class_method = colorby['class_method']
        if 'class_number' in colorby:
            class_number = colorby['class_method']
        if 'color_map' in colorby:
            color_map = colorby['color_map']

        vallist = []
        colrec = {}
        for key, val in recs.iteritems():
            cval = val[ind]
            colrec[key] = cval
            vallist.append(cval)
        bmap = brewer2mpl.get_map(color_map, 'Sequential', class_number)
        self.colorlist = bmap.colors

        ncuts = numeric_cuts(vallist, class_method, class_number)
        self.cuts = ncuts.cuts

    def getcolordict(self):
        colordict = {}

        self.colordict = colordict
        return colordict


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