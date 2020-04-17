########################################################################################################################
# Support Package for MyXUO v1.0
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
import art
import online
import pages
import std
import format
import animate

__XLIB_TARGET = 'MyXUO'
__LICENSE_HEAD = '''
Support Package for MyXUO v1.0

(C) 2020 XUOGROUP, all rights reserved.
This software is released under a GNU GPL v3.0 License.
Please READ it before you redistribute this software.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Follow us on <http://www.xuogroup.top>!
Thank you for choosing XUOGROUP software!'''


def get_xlib_target():
    return __XLIB_TARGET


if __name__ == '__main__':
    print __LICENSE_HEAD
    reply = raw_input('< Press [enter] to quit or enter [c] to read the full version of the license >')
    if reply.lower()[0] == 'c':
        try:
            license_full_f = open('../LICENSE')
            license_full = license_full_f.readlines()
            for string in license_full:
                print string.strip()
            raw_input('< Press [enter] to quit. Thank you for visiting! >')
        except IOError:
            print 'LICENSE not found.'
            print 'You can visit http://www.gnu.org/licenses/ and read the content of General Public License v3.0.'
            raw_input('< Press [enter] to quit >')
