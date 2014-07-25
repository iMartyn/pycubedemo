# Display message a character at a time
# Copyright (C) Paul Brook <paul@nowt.org>
# Released under the terms of the GNU General Public License version 3

import cubehelper
import font
import random
import math
import argparse

class Pattern(object):
    def init(self,args = None):
        self.message = 'Hello World'
        self.color = -1
        if (args is not None) and (args.message is not None):
            self.message = args.message
            color_mapping = [ ('#red', 0xff0000), ('#green', 0x00ff00), ('#blue', 0x0000ff), ('#white', 0xffffff) ]
            for hashtag, color in color_mapping:
                if hashtag in self.message:
                    self.message = self.message.replace(hashtag, '')
                    self.color = color
        self.position = 0
        self.double_buffer = True
        return 0.5 / self.cube.size
    def tick(self):
        self.cube.clear()
        if self.position == 0:
            if self.message == '':
                raise StopIteration
            c = self.message[0]
            self.message = self.message[1:]
            n = ord(c) - 32
            if n >= 0 and n < len(font.font_data):
                self.data = font.font_data[n]
            else:
                self.data = ()
            if self.color == -1:
                self.color = cubehelper.random_color()
        x = (self.cube.size - len(self.data)) // 2
        y = self.position
        for mask in self.data:
            for z in range(0, 8):
                if mask & (0x80 >> z):
                    color = self.color
                else:
                    color = (0,0,0)
                self.cube.set_pixel((x, y, z), color)
            x += 1
        self.position += 1
        if self.position == self.cube.size:
            self.position = 0
