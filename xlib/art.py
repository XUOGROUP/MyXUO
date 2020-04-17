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

from ast import literal_eval
import ConfigParser as Cp

MY_COLORS = {}

try:
    reader = Cp.ConfigParser()
    reader.read('./res/config/artmd.ini')
    items = reader.items('colors')
    for i in items:
        if not i[0] in MY_COLORS:
            MY_COLORS[i[0]] = literal_eval(i[1])
except Cp.Error:
    pass


def get_colors(color):
    try:
        return MY_COLORS[color][:]
    except KeyError:
        return [0, 0, 0, 0]
