#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2019  <pi@thepoet>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

#
from Adafruit_Thermal import *
printer = Adafruit_Thermal("/dev/serial0", 9600, timeout=1)

def main():
    #poem = generatePoem(25)
    poem = '1, 2, 3, 4...'

    testing(poem)
    return 0


def testing(poem):
    printer.wake()
    printer.setSize('S')
    printer.println(poem)
    printer.feed(1)

    print('aa')

    printer.setDefault()
    printer.sleep()

main()
