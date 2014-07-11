# Plasma spiral (really a cylinder...)
# Copyright (C) Martyn Ranyard <martyn@ranyard.info>
# Released under the terms of the GNU General Public License version 3

import random
import cubehelper
import math

IQ = 10

INITIAL_ENERGY = 1.0
MINSIZE = 4

def color_from_val(val):
    if val < 85:
        r = val * 3;
        g = 255 - r;
        b = 0;
    elif val < 170:
        b = (val - 85) * 3;
        r = 255 - b;
        g = 0;
    else:
        g = (val - 170) * 3;
        b = 255 - g;
        r = 0;
    return (r, g, b)

class Pattern(object):
    def init(self):
        self.position = 0
        self.colorpoint = 0
        return 0.0001

    def polar_to_xy(self,degrees,distance):
        x = distance * math.cos(math.radians(degrees))
        y = distance * math.sin(math.radians(degrees))
        return (int(x),int(y))

    def fill_point(self,i):
        halfcube = int(self.cube.size/2)
        color = color_from_val(((255/self.cube.size**2)*self.colorpoint % 255))
        deg = (360/self.cube.size-1)*(i%self.cube.size)
        x,z = self.polar_to_xy(deg,halfcube)
        x = x + halfcube -1
        z = z + halfcube -1
        y = int(i / self.cube.size)
        self.cube.set_pixel((x,y,z),color)

    def tick(self):
        self.fill_point(self.position)
        self.position += 1
        self.colorpoint += 1
        if self.position == self.cube.size**2:
            self.colorpoint += 5
            self.position = 0
        return False
