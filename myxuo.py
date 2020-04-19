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
import sys
import os
import xlib

# Import modules


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    # Init pygame

    os.environ['SDL_VIDEO_WINDOW_POS'] = '%d, %d' % xlib.format.SCREEN_LOCATION

    # Set window location

    screen_main = pygame.display.set_mode(xlib.format.SCREEN_SIZE)
    screen_main_rect = screen_main.get_rect()

    alpha_main = screen_main.convert_alpha()
    alpha_main_rect = alpha_main.get_rect()

    pygame.display.set_caption(xlib.format.SCREEN_TITLE)
    main_icon = pygame.image.load(xlib.pages.SCREEN_ICON)
    pygame.display.set_icon(main_icon)
    # Create screens
    start_page = xlib.pages.StartPage(alpha_main)
    start_page.draw()
    pygame.display.update()
    # start page

    screen_main.blit(alpha_main, [0, 0])
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    pygame.quit()
    sys.exit(0)
