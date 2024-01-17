# -*- coding: utf-8 -*-

def get_loc(loc):
    xyloc = None
    ta = None
    if loc=='top_left':
        xyloc = ['5%','5%']
        ta = 'start'
    elif loc=='top_right':
        xyloc = ['95%','5%']
        ta = 'end'
    elif loc=='bottom_left':
        xyloc = ['5%','95%']
        ta = 'start'
    elif loc=='bottom_right':
        xyloc = ['95%','95%']
        ta = 'end'
    elif loc=='top_middle':
        xyloc = ['50%','5%']
        ta = 'middle'
    elif loc=='bottom_middle':
        xyloc = ['50%','95%']
        ta = 'middle'
    else:
        print('location problem')
    return (xyloc, ta)

def get_loc2(loc):
    xyloc = None
    ta = None
    if loc=='left':
        xyloc = ['5%','50%']
        ta = 'start'
    elif loc=='right':
        xyloc = ['75%','50%']
        ta = 'start'
    elif loc=='middle':
        xyloc = ['30%','50%']
        ta = 'start'
    else:
        print('location problem')
    return (xyloc, ta)
