# Plasma spiral (really a cylinder...)
# Copyright (C) Martyn Ranyard <martyn@ranyard.info>
# Released under the terms of the GNU General Public License version 3

import random
import cubehelper
import math
import numpy

PATTERN0 = numpy.array([
    [ 0.,  0.,  1.,  1.,  0.,  0.,  0.,  0.],
    [ 0.,  1.,  0.,  0.,  0.,  1.,  1.,  0.],
    [ 0.,  1.,  1.,  0.,  1.,  1.,  0.,  1.],
    [ 0.,  0.,  1.,  1.,  1.,  0.,  0.,  1.],
    [ 1.,  0.,  0.,  1.,  1.,  1.,  0.,  0.],
    [ 1.,  0.,  1.,  1.,  0.,  1.,  1.,  0.],
    [ 0.,  1.,  1.,  0.,  0.,  0.,  1.,  0.],
    [ 0.,  0.,  0.,  0.,  1.,  1.,  0.,  0.]])

PATTERN1 = numpy.array([
    [ 0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.],
    [ 0.,  1.,  0.,  0.,  1.,  0.,  1.,  0.],
    [ 1.,  0.,  0.,  0.,  1.,  0.,  0.,  0.],
    [ 0.,  1.,  1.,  1.,  1.,  0.,  0.,  0.],
    [ 0.,  0.,  0.,  1.,  1.,  1.,  1.,  0.],
    [ 0.,  0.,  0.,  1.,  0.,  0.,  0.,  1.],
    [ 0.,  1.,  0.,  1.,  0.,  0.,  1.,  0.],
    [ 0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.]])

PATTERN2 = numpy.array([
    [ 0.,  0.,  0.,  1.,  1.,  1.,  1.,  0.],
    [ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.],
    [ 1.,  0.,  0.,  1.,  0.,  0.,  0.,  0.],
    [ 1.,  0.,  0.,  1.,  1.,  1.,  1.,  1.],
    [ 1.,  1.,  1.,  1.,  1.,  0.,  0.,  1.],
    [ 0.,  0.,  0.,  0.,  1.,  0.,  0.,  1.],
    [ 0.,  0.,  0.,  0.,  1.,  0.,  0.,  1.],
    [ 0.,  1.,  1.,  1.,  1.,  0.,  0.,  0.]])

PATTERN3 = numpy.array([
    [ 0.,  0.,  1.,  1.,  1.,  0.,  0.,  0.],
    [ 0.,  0.,  1.,  0.,  0.,  0.,  0.,  0.],
    [ 0.,  0.,  1.,  1.,  0.,  1.,  1.,  1.],
    [ 1.,  0.,  0.,  1.,  1.,  1.,  0.,  1.],
    [ 1.,  0.,  1.,  1.,  1.,  0.,  0.,  1.],
    [ 1.,  1.,  1.,  0.,  1.,  1.,  0.,  0.],
    [ 0.,  0.,  0.,  0.,  0.,  1.,  0.,  0.],
    [ 0.,  0.,  0.,  1.,  1.,  1.,  0.,  0.]])

PATTERNCOUNT = 3
PATTERNS = numpy.array([PATTERN0,PATTERN1,PATTERN2,PATTERN3])
STEP = 2

def color_from_val(val):
    while val < 0:
        val += 255
    if val > 255:
        val = val % 255
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
        FPS = 2
        CALLEDPERSEC = 1./FPS
        return CALLEDPERSEC

    def tick(self):
        self.cube.clear()
        cubesize = self.cube.size
        for z in range(0,cubesize):
            for x in range(0,cubesize):
                for y in range(0,cubesize):
                    offset = z//STEP
                    plane = self.position - offset
                    if plane > PATTERNCOUNT:
                        plane = plane % PATTERNCOUNT
                    while plane < 0:
                        plane += PATTERNCOUNT+1
                    if PATTERNS[plane][x,y] > 0:
                        self.cube.set_pixel((x,z,y),color_from_val(self.colorpoint-(z*(255/cubesize))))
        self.position += 1
        if self.position > cubesize:
            self.position -= cubesize
        self.colorpoint += cubesize+1
        if self.colorpoint > 255:
            self.colorpoint = 0
        return False
