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
import xml.etree.cElementTree as Et
import art

SCREEN_ICON = './res/assets/XIcon.png'


class StartPage:
    def __init__(self, screen):
        self.SCREEN = screen

    def draw(self, screen=None, x_m_h=75, x_m_v=-60, m_m_h=-175, m_m_v=-100, f_m_h=0, f_m_v=50, m_s=100,
             f_s=42, l_m_h=0, l_m_v=130, l_s=36):
        if screen is None:
            screen = self.SCREEN

        xuo_margin_horizontal = x_m_h
        xuo_margin_vertical = x_m_v
        my_margin_horizontal = m_m_h
        my_margin_vertical = m_m_v
        footer_margin_horizontal = f_m_h
        footer_margin_vertical = f_m_v
        load_margin_horizontal = l_m_h
        load_margin_vertical = l_m_v
        my_size = m_s
        footer_size = f_s
        load_size = l_s

        page_root = Et.parse('./res/xml/style.xml').getroot().find('pages').find('start')

        screen.fill(art.get_colors(page_root.find('bg_color').text))
        # Fill screen

        screen_center = screen.get_rect().center

        xuo_logo_white = pygame.image.load('./res/assets/XUOIcon-White.png')
        xuo_logo_white_rect = xuo_logo_white.get_rect()
        xuo_logo_white_rect.center = (screen_center[0] + xuo_margin_horizontal,
                                      screen_center[1] + xuo_margin_vertical)

        # Render icon 'XUO'

        font = pygame.font.SysFont(
            page_root.find('my_font').text, my_size)
        myxuo_text = font.render('My', True, art.get_colors(page_root.find('my_color').text))
        myxuo_rect = myxuo_text.get_rect()
        myxuo_rect.center = (screen_center[0] + my_margin_horizontal,
                             screen_center[1] + my_margin_vertical)
        # Render text 'My'

        footer = pygame.font.SysFont(
            page_root.find('footer_font').text, footer_size)
        footer_text = footer.render('XUOGROUP PRESENTS', True,
                                    art.get_colors(page_root.find('footer_color').text))
        footer_rect = footer_text.get_rect()
        footer_rect.center = (screen_center[0] + footer_margin_horizontal,
                              screen_center[1] + footer_margin_vertical)
        # Render footer

        load = pygame.font.SysFont(
            page_root.find('load_font').text, load_size)
        footer_text = footer.render('XUOGROUP PRESENTS', True,
                                    art.get_colors(page_root.find('footer_color').text))
        load_text = load.render(u'正在加载……', True, art.get_colors(page_root.find('load_color').text))
        load_rect = load_text.get_rect()
        load_rect.center = (screen_center[0] + load_margin_horizontal,
                            screen_center[1] + load_margin_vertical)
        # Render load text

        screen.blit(xuo_logo_white, xuo_logo_white_rect)
        screen.blit(myxuo_text, myxuo_rect)
        screen.blit(footer_text, footer_rect)
        screen.blit(load_text, load_rect)
        # screen blit
