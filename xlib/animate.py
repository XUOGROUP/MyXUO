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
import pygame

NORMAL_FPS = 30
RAPID_FPS = 60


def new_clock():
    clock = pygame.time.Clock()
    return clock


def switch_in(display_screen, alpha_screen, bg_color, font, font_color, margin=20, fps=NORMAL_FPS):
    clock = new_clock()
    for alpha in range(0, 128, 2):
        p_color = [bg_color[0], bg_color[1], bg_color[2], alpha]
        f_color = font_color
        text = font.render(u'正在加载……', True, f_color)
        font_rect = text.get_rect()
        font_rect.center = (alpha_screen.get_rect().center[0], alpha_screen.get_rect().center[1] + margin)
        alpha_screen.fill(p_color)
        alpha_screen.blit(text, font_rect)
        pygame.event.get()
        display_screen.blit(alpha_screen, (0, 0))
        pygame.display.update()
        clock.tick(fps)
