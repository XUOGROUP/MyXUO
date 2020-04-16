# -*- coding:utf-8 -*-
########################################################################################################################
# Main script for MyXUO v1.0
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

import pygame
import copy
import urllib2
import requests
import random
import xml.etree.cElementTree as Et
import ConfigParser as Cp
import os
import sys
from ast import literal_eval

sys.path.append('./lib/')

try:
    import xuogroup_online
except ImportError:
    pass
# Import modules


MY_COLORS = {}
SCREEN_SIZE = [1024, 768]


def start_page(screen):

    my_margin_horizontal = 75
    my_margin_vertical = 100
    xuo_margin_horizontal = 75
    xuo_margin_vertical = 100

    screen.fill(get_colors(Et.parse(
        '../res/xml/style.xml').getroot().find('pages').find('start').find('bg_color').text))
    # Fill screen

    xuo_logo_white = pygame.image.load('../res/assets/XUOIcon-White.png')
    xuo_logo_white_rect = xuo_logo_white.get_rect()
    xuo_logo_white_rect.center = (screen.get_rect().center[0] + xuo_margin_horizontal,
                                  screen.get_rect().center[1] + xuo_margin_vertical)

    font = pygame.font.SysFont(
        Et.parse('../res/xml/style.xml').getroot().find('pages').find('start').find('font').text, 100)
    myxuo_text = font.render('My', True, get_colors('white'))
    myxuo_rect = myxuo_text.get_rect()
    myxuo_rect.center = (screen.get_rect().center[0] + my_margin_horizontal,
                         screen.get_rect().center[1] + my_margin_vertical)
    screen.blit(myxuo_text, myxuo_rect)
    screen.blit(xuo_logo_white, xuo_logo_white_rect)


def append_colors(colors, path):
    try:
        reader = Cp.ConfigParser()
        reader.read(path)
        items = reader.items('colors')
        for i in items:
            if not i[0] in colors:
                colors[i[0]] = literal_eval(i[1])
    except Cp.Error:
        pass


def get_colors(color):
    try:
        return MY_COLORS[color][:]
    except KeyError:
        return [0, 0, 0, 0]


def switch_page(screen, page):
    pass


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    # Init pygame

    current_window = 'start'

    append_colors(MY_COLORS, '../res/raw/art.ini')

    # Load files
    screen_main = pygame.display.set_mode(SCREEN_SIZE)
    screen_main_rect = screen_main.get_rect()
    alpha_main = screen_main.convert_alpha()
    alpha_main_rect = alpha_main.get_rect()

    pygame.display.set_caption('MyXUO')
    # Create screens

    # start page

    start_page(alpha_main)
    screen_main.blit(alpha_main, [0, 0])
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    pygame.quit()
    sys.exit(0)
