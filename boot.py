# -*- coding:utf-8 -*-
########################################################################################################################
# Boot Program for MyXUO v1.0
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
import sys
import os.path
import traceback
import datetime
from os import execv
# Import modules
try:
    assert os.path.exists('./res/assets/XIcon.png')
    assert os.path.exists('./res/assets/XUOIcon-White.png')
    assert os.path.exists('res/config/artmd.ini')
    assert os.path.exists('./res/sound/index.ini')
    assert os.path.exists('./res/xml/rules.xml')
    assert os.path.exists('./res/xml/rules.xml')
    assert os.path.exists('./xlib/__init__.py')
    assert os.path.exists('./xlib/art.py')
    assert os.path.exists('./xlib/animate.py')
    assert os.path.exists('./xlib/format.py')
    assert os.path.exists('./xlib/pages.py')
    assert os.path.exists('./xlib/online.py')
    assert os.path.exists('./xlib/std.py')
    assert os.path.exists('LICENSE')
    assert os.path.exists('./res/font/NotoSansHans-Light.otf')
    assert os.path.exists('./res/font/NotoSansHans-Black.otf')
    assert os.path.exists('./res/font/NotoSansHans-Bold.otf')
    assert os.path.exists('./res/font/NotoSansHans-DemiLight.otf')
    assert os.path.exists('./res/font/NotoSansHans-Medium.otf')
    assert os.path.exists('./res/font/NotoSansHans-Regular.otf')
    assert os.path.exists('./res/font/NotoSansHans-Thin-Windows.otf')
    execv('./myxuo.exe', ['myxuo.exe'])


except (AssertionError, OSError), e:
    f = open('./Error.log', 'w')
    f.write(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    f.write('\n')
    f.write('An error occurred, please check if you have deleted any file.\n')
    f.write('Exception Found:\n\n')
    f.write(str(traceback.format_exc()))
    f.write('\n')
    f.close()
    sys.exit(1)
except WindowsError:
    pass
