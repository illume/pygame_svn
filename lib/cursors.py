##    PyGame - Python Game Library
##    Copyright (C) 2000  Pete Shinners
##
##    This library is free software; you can redistribute it and/or
##    modify it under the terms of the GNU Library General Public
##    License as published by the Free Software Foundation; either
##    version 2 of the License, or (at your option) any later version.
##
##    This library is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
##    Library General Public License for more details.
##
##    You should have received a copy of the GNU Library General Public
##    License along with this library; if not, write to the Free
##    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
##
##    Pete Shinners
##    pete@shinnerso.org

"""Set of cursor resources available for use. These cursors come
in a sequence of values that are needed as the arguments for
pygame.mouse.set_cursor(). to dereference the sequence in place
and create the cursor in one step, call like this;
pygame.mouse.set_cursor(*pygame.cursors.arrow)"""

#default pygame black arrow
arrow = ((16, 16), (0, 0),
    (0x00,0x00,0x40,0x00,0x60,0x00,0x70,0x00,0x78,0x00,0x7C,0x00,0x7E,0x00,0x7F,0x00,
     0x7F,0x80,0x7C,0x00,0x6C,0x00,0x46,0x00,0x06,0x00,0x03,0x00,0x03,0x00,0x00,0x00),
    (0x40,0x00,0xE0,0x00,0xF0,0x00,0xF8,0x00,0xFC,0x00,0xFE,0x00,0xFF,0x00,0xFF,0x80,
     0xFF,0xC0,0xFF,0x80,0xFE,0x00,0xEF,0x00,0x4F,0x00,0x07,0x80,0x07,0x80,0x03,0x00))

diamond = ((16, 16), (7, 7),
    (0x00, 0x00, 0x80, 0x00, 0xc0, 0x01, 0x60, 0x03, 0x30, 0x06, 0x18, 0x0c,
     0x0c, 0x18, 0x06, 0x30, 0x0c, 0x18, 0x18, 0x0c, 0x30, 0x06, 0x60, 0x03,
     0xc0, 0x01, 0x80, 0x00, 0x00, 0x00, 0x00, 0x00),
    (0x80, 0x00, 0xc0, 0x01, 0xe0, 0x03, 0xf0, 0x07, 0x78, 0x0f, 0x3c, 0x1e,
     0x1e, 0x3c, 0x0f, 0x78, 0x1e, 0x3c, 0x3c, 0x1e, 0x78, 0x0f, 0xf0, 0x07,
     0xe0, 0x03, 0xc0, 0x01, 0x80, 0x00, 0x00, 0x00))




