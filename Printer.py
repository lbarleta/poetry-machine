from PIL import Image
from thermalprinter import *

with ThermalPrinter(port='/dev/serial0', baudrate=9600) as printer:
    # Bar codes
    printer.image(Image.open('gnu.png'))

    # Styles
    printer.out('Bold', bold=True)

    printer.feed(2)
