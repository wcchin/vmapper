# -*- coding: utf-8 -*-

class Layer:
    def __init__(self, layername):
        self.layername = layername
        self.features = []

    def addtoLayer(self, item):
        self.features.append(item)

    def get_layer_str(self):
        strs = ''
        strslist = [ f.feature_string() for f in self.features ]
        strs = ' '.join(strslist)
        return strs
