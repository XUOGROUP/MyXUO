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
    execv('./myxuo.exe', ['myxuo.exe'])
except (AssertionError, OSError):
    sys.exit(3221225794)

