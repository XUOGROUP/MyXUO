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
import animate

SCREEN_ICON = './res/assets/XIcon.png'


class StartPage:
    def __init__(self, screen):
        self.SCREEN = screen
        self.done = False
        self.uis = {}
        self.music = ''

    def draw(self, screen=None, text=u'', x_m_h=120, x_m_v=-70, m_m_h=-250, m_m_v=-160, f_m_h=0, f_m_v=75, m_s=120,
             f_s=42, l_m_h=0, l_m_v=155, l_s=36):

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
        xuo_size = (543, 125)

        if screen is None:
            screen = self.SCREEN

        page_root = Et.parse('./res/xml/style.xml').getroot().find('pages').find('start')

        screen.fill(art.get_colors(page_root.find('bg_color').text))
        # Fill screen

        screen_center = screen.get_rect().center

        xuo_logo_white = pygame.transform.scale(pygame.image.load('./res/assets/XUOIcon-White.png'), xuo_size)
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

        footer = pygame.font.Font(
            page_root.find('footer_font').text, footer_size)
        footer_text = footer.render('XUOGROUP PRESENTS', True,
                                    art.get_colors(page_root.find('footer_color').text))
        footer_rect = footer_text.get_rect()
        footer_rect.center = (screen_center[0] + footer_margin_horizontal,
                              screen_center[1] + footer_margin_vertical)
        # Render footer

        load = pygame.font.Font(
            page_root.find('load_font').text, load_size)
        footer_text = footer.render('XUOGROUP PRESENTS', True,
                                    art.get_colors(page_root.find('footer_color').text))
        if self.done:
            load_text = load.render(u'点击屏幕开始游戏', True, art.get_colors(page_root.find('load_color').text))
        else:
            load_text = load.render(u'正在载入……', True, art.get_colors(page_root.find('load_color').text))
        load_rect = load_text.get_rect()
        load_rect.center = (screen_center[0] + load_margin_horizontal,
                            screen_center[1] + load_margin_vertical)
        # Render load text

        screen.blit(xuo_logo_white, xuo_logo_white_rect)
        screen.blit(myxuo_text, myxuo_rect)
        screen.blit(footer_text, footer_rect)
        screen.blit(load_text, load_rect)
        # screen blit

    def load(self):
        ui_size = (50, 50)
        box_size = (15, 15)
        if self.done:
            pass
        else:
            self.uis = {'back': pygame.transform.scale(pygame.image.load('./res/ui/ui_back.png'), ui_size),
                        'next': pygame.transform.scale(pygame.image.load('./res/ui/ui_next.png'), ui_size),
                        'up': pygame.transform.scale(pygame.image.load('./res/ui/ui_up.png'), ui_size),
                        'down': pygame.transform.scale(pygame.image.load('./res/ui/ui_down.png'), ui_size),
                        'checkbox': {
                            'on': pygame.transform.scale(pygame.image.load('./res/ui/ui_checkbox.png'), box_size),
                            'off': pygame.transform.scale(
                                pygame.image.load('./res/ui/ui_checkbox_off.png'), box_size)
                            },
                        'radiobutton': {'on': pygame.transform.scale(pygame.image.load('./res/ui/ui_radiobutton.png'),
                                                                     box_size),
                                        'off': pygame.transform.scale(
                                            pygame.image.load('./res/ui/ui_radiobutton_off.png'), box_size)
                                        },
                        'yes': {'off': pygame.transform.scale(pygame.image.load('./res/ui/ui_yes.png'),
                                                              ui_size),
                                'hover': pygame.transform.scale(
                                    pygame.image.load('./res/ui/ui_yes_hover.png'), ui_size)
                                },
                        'no': {'off': pygame.transform.scale(pygame.image.load('./res/ui/ui_no.png'),
                                                             ui_size),
                               'hover': pygame.transform.scale(
                                   pygame.image.load('./res/ui/ui_no_hover.png'), ui_size)
                               }, 'ok': {'off': pygame.transform.scale(pygame.image.load('./res/ui/ui_ok.png'),
                                                                       ui_size),
                                         'hover': pygame.transform.scale(
                                             pygame.image.load('./res/ui/ui_ok_hover.png'), ui_size)
                                         }}
            self.done = True
        return self.uis


class MainMenuPage:
    def __init__(self, screen):
        self.SCREEN = screen

    def draw(self, screen, main):
        if screen is None:
            screen = self.SCREEN
        page_root = Et.parse('./res/xml/style.xml').getroot().find('pages').find('mainmenu')
        bg_color = art.get_colors(page_root.find('bg_color').text)[:]
        text_color = art.get_colors('white')[:]
        t_font = pygame.font.Font(page_root.find('font').text, 50)
        scr_rect = screen.get_rect()
        clock = animate.new_clock()
        for alpha in range(0, 255, 5):
            pygame.event.get()
            bg_color[3] = alpha
            screen.fill(bg_color)
            main.blit(screen, (0, 0))
            pygame.display.update()
            clock.tick(animate.RAPID_FPS)
        new_text = t_font.render(u'新战役', True, text_color)
        load_text = t_font.render(u'载入存储游戏', True, text_color)
        shop_text = t_font.render(u'商店', True, text_color)
        set_text = t_font.render(u'选项', True, text_color)
        exit_text = t_font.render(u'退出', True, text_color)
        new_rect = new_text.get_rect()
        load_rect = load_text.get_rect()
        shop_rect = shop_text.get_rect()
        set_rect = set_text.get_rect()
        exit_rect = exit_text.get_rect()
        ct = scr_rect.center
        new_rect.center = (ct[0], ct[1] - 200)
        load_rect.center = (ct[0], ct[1] - 100)
        shop_rect.center = ct
        set_rect.center = (ct[0], ct[1] + 100)
        exit_rect.center = (ct[0], ct[1] + 200)
        screen.blit(new_text, new_rect)
        screen.blit(load_text, load_rect)
        screen.blit(shop_text, shop_rect)
        screen.blit(set_text, set_rect)
        screen.blit(exit_text, exit_rect)
        main.blit(screen, (0, 0))
