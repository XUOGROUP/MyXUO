# -*- coding:utf-8 -*-
########################################################################################################################
# Support Modules for MyXUO v1.0
#
# (C) 2020 XUOGROUP, all rights reserved.
# This software is released under a GNU GPL v3.0 License. Please READ it before you redistribute this software.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Follow us on <http://www.xuogroup.top>!
# Thank you for choosing XUOGROUP software!
########################################################################################################################
import gc


def trans_grid(width, height, rows, columns, square=True):
    wid = width / columns
    hei = height / rows
    pmap = []
    if square:
        size = max(wid, hei)
        c = width / size
        r = height / size

        for i in range(c):
            pmap[i] = []
            for j in range(r):
                pmap[i][j] = '.keep'
        s = [size, size]

    else:

        for i in range(columns):
            pmap[i] = []
            for j in range(rows):
                pmap[i][j] = '.keep'
        s = [wid, hei]
    return [s, pmap]
# Transform screen to grid and return both size and the map.
# 'map' is a built-in name so we use 'pmap' instead of 'map'.


def destroy(target):
    del target
    gc.collect()


def isIn(point, rect):
    x, y = point
    x = int(x)
    y = int(y)
    # Rect should be: (left, top, width, height)
    if int(rect[0]) <= x <= int(rect[0]) + int(rect[2]):
        if int(rect[1]) <= y <= int(rect[1] + int(rect[3])):
            return True
        else:
            return False
    else:
        return False
