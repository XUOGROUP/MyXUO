# -*- coding:utf-8 -*-
########################################################################################################################
# Boot loader for MyXUO v1.0
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
import webbrowser

from PyQt4 import QtGui, uic, QtCore
import gc
import requests
import sys
import os
import ConfigParser as Cp

if __name__ == '__main__':

    URL = 'http://tinywebdb.appinventor.space/api'
    WEB = 'http://www.xuogroup.top'
    CONFIG = Cp.ConfigParser()
    CONFIG.read('./lib/config.ini')

    form_class, base_class = uic.loadUiType('./res/layout/Login.ui')
    app = QtGui.QApplication(sys.argv)


    def web():
        webbrowser.open_new_tab(WEB)


    class Login(base_class, form_class):

        def __init__(self, config):
            base_class.__init__(self, parent=None)
            self.setupUi(self)
            self.xid = ''

            try:
                icon_w = QtGui.QIcon(config.get('fat', 'icon_w'))
            except Cp.NoSectionError or Cp.NoOptionError:
                win = QtGui.QMessageBox()
                win.setIcon(QtGui.QMessageBox.Critical)
                win.setWindowTitle(u'错误')
                win.setWindowIcon(QtGui.QIcon('./res/assets/XIcon.png'))
                win.setText(u'MyXUO遇到严重错误，可能无法正常运行。\n请自游戏光盘或者软件包重新安装程序。\n\n'
                            u'错误：ERR_WRONG_FAT\n若要以开发人员模式继续，单击“尝试继续”；否则，单击“终止程序”。\n')
                win.addButton(u'终止程序', QtGui.QMessageBox.YesRole)
                win.setWindowIcon(self.icon)
                win.addButton(u'尝试继续', QtGui.QMessageBox.NoRole)
                result = win.exec_()
                if result == 0:
                    gc.collect()
                    sys.exit(1)
                icon_w = QtGui.QIcon('./res/assets/XIcon.png')

            self.setWindowIcon(icon_w)

            # Try to load Picture of XUO
            try:
                ico = QtGui.QIcon(config.get('fat', 'icon_x'))
                ico.addPixmap(QtGui.QPixmap(config.get('fat', 'icon_x')), QtGui.QIcon.Disabled, QtGui.QIcon.Off)
            except Cp.NoSectionError or Cp.NoOptionError:
                win = QtGui.QMessageBox()
                win.setIcon(QtGui.QMessageBox.Critical)
                win.setWindowTitle(u'错误')
                win.setWindowIcon(QtGui.QIcon('./res/assets/XIcon.png'))
                win.setText(u'MyXUO遇到严重错误，必须现在退出。\n请自游戏光盘或者软件包重新安装程序。\n\n'
                            u'错误：ERR_NO_ICON')
                win.setWindowIcon(self.icon)
                win.addButton(u'终止程序', QtGui.QMessageBox.AcceptRole)
                win.exec_()
                gc.collect()
                sys.exit(1)

            self.Pic.setIcon(ico)
            self.Pic.setToolTip(u'前往XUOGROUP')
            self.Pic.setCursor(QtCore.Qt.PointingHandCursor)
            self.Submit.setCursor(QtCore.Qt.PointingHandCursor)
            try:
                self.id = config.get('account', 'id')
            except Cp.NoSectionError or Cp.NoOptionError:
                self.id = ''
            if id != '' and id is not None:
                self.ID.setText(self.id)
            else:
                self.ID.setText('')
            self.ID.setToolTip(u'此处输入您的XUOGROUP ID')
            self.icon = icon_w
            self.Password.setToolTip(u'此处输入您的密码，密码无回显')
            self.Pic.clicked.connect(web)
            self.Submit.clicked.connect(self.log_in)

        def log_in(self):
            gc.collect()
            xid = self.ID.text()
            psw = self.Password.text()
            if xid != '' and psw != '' and len(psw) >= 6:
                try:
                    href = {'user': 'myxuo', 'secret': 'f5623fa8', 'action': 'get', 'tag': str(self.ID.text())}
                    res = requests.post(URL, href).text
                    c_psw = res.split('"')[3]
                    if c_psw == 'null':
                        win = QtGui.QMessageBox()
                        win.setIcon(QtGui.QMessageBox.Warning)
                        win.setWindowTitle(u'注册吗？')
                        win.setText(u'XUOGROUP的数据库中无此用户。\n要注册吗？\n\n请妥善保管您的密码，如若遗忘，XUOGROUP无法帮您找回！')
                        win.addButton(u'注册', QtGui.QMessageBox.YesRole)
                        win.setWindowIcon(self.icon)
                        win.addButton(u'我手滑', QtGui.QMessageBox.NoRole)
                        reply = win.exec_()
                        if reply == 0:
                            href['action'] = 'update'
                            href['value'] = str(self.Password.text())
                            requests.post(URL, href)
                            win = QtGui.QMessageBox()
                            win.setWindowIcon(self.icon)
                            win.setWindowTitle(u'注册成功')
                            win.setIcon(QtGui.QMessageBox.Information)
                            win.setText(u'欢迎你，' + xid + u'。\n注册完成，请继续登录。')
                            win.addButton(u'好', QtGui.QMessageBox.YesRole)
                            win.exec_()
                    else:
                        if c_psw == psw:
                            self.xid = xid
                            win = QtGui.QMessageBox()
                            win.setIcon(QtGui.QMessageBox.Information)
                            win.setText(u'欢迎回来，' + xid + u'！')
                            win.setWindowTitle(u'欢迎')
                            win.setWindowIcon(self.icon)
                            win.addButton(u'开始游戏', QtGui.QMessageBox.YesRole)
                            win.exec_()
                            gc.collect()
                            # os.execv('./bin/myxuo.exe', ['MyXUO', self.xid])
                            sys.exit(0)
                        else:
                            self.Password.setText('')
                            win = QtGui.QMessageBox()
                            win.setIcon(QtGui.QMessageBox.Critical)
                            win.setWindowTitle(u'密码错误')
                            win.setText(u'XUOGROUP ID或密码错误。\n检查你的拼写，然后重试。')
                            win.addButton(u'好', QtGui.QMessageBox.AcceptRole)
                            win.setWindowIcon(self.icon)
                            win.exec_()

                except requests.HTTPError or requests.ConnectionError:
                    win = QtGui.QMessageBox()
                    win.setIcon(QtGui.QMessageBox.Critical)
                    win.setWindowTitle(u'错误')
                    win.setText(u'你尚未联机，或服务器不可用。\nWeb因你而不同。\n\n错误：ERR_HTTP_NO_RESPONSE')
                    win.addButton(u'重试', QtGui.QMessageBox.YesRole)
                    win.addButton(u'放弃', QtGui.QMessageBox.NoRole)
                    win.setWindowIcon(self.icon)
                    reply = win.exec_()
                    if reply == 1:
                        gc.collect()
                        sys.exit(0)

            else:
                win = QtGui.QMessageBox()
                win.setIcon(QtGui.QMessageBox.Critical)
                win.setWindowTitle(u'错误')
                win.setWindowIcon(self.icon)
                win.setText(u'用户名密码不能为空，密码不能小于6位。')
                win.addButton(u'好', QtGui.QMessageBox.AcceptRole)
                win.exec_()


    window = Login(CONFIG)
    window.show()
    app.exec_()
