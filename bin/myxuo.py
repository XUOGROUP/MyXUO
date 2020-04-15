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
# Thank you for choosing XUOGROUP software!
########################################################################################################################

import pygame
import urllib2
import requests
import random
import xml.etree.cElementTree as Et
import os
import sys


class Img:
    def __init__(self, path):
        self.img = pygame.image.load(path)
        self.rect = self.img.get_rect()
        self.width = self.rect.width
        self.height = self.rect.height

    def cal_position(self, center):
        width = self.width
        height = self.height
        return [center[0] - (width / 2), center[1] - (height / 2)]


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    # Init pygame
    screen = pygame.display.set_mode([640, 480])
    screen.fill([11, 187, 255])
    pygame.display.set_caption('MyXUO')
    # Init screen

    current_window = 'start'
    xuo_logo_white = Img('../res/assets/XUOIcon-White.png')
    screen.blit(xuo_logo_white.img, xuo_logo_white.cal_position([320, 240]))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    pygame.quit()
