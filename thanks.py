# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This test will initialize the display using displayio and draw a solid green
background, a smaller purple rectangle, and some yellow text.
"""
import board
import terminalio
import displayio

# Starting in CircuitPython 9.x fourwire will be a seperate internal library
# rather than a component of the displayio library
try:
    from fourwire import FourWire
except ImportError:
    from displayio import FourWire
from adafruit_display_text import label
from adafruit_st7789 import ST7789

# First set some parameters used for shapes and text
BORDER = 20
FONTSCALE = 2
BACKGROUND_COLOR = 0xebd234  # Bright Green
FOREGROUND_COLOR = 0xebd234  # Purple
TEXT_COLOR = 0xebd234

# Release any resources currently in use for the displays
displayio.release_displays()

spi = board.SPI()
tft_cs = board.D2
tft_dc = board.D3

display_bus = FourWire(spi, command=tft_dc, chip_select=tft_cs)
display = ST7789(
    display_bus, rotation=270, width=240, height=135, rowstart=40, colstart=53
)

from adafruit_display_shapes.rect import Rect
from adafruit_display_shapes.circle import Circle
from adafruit_display_shapes.roundrect import RoundRect
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.polygon import Polygon

# Make the display context
splash = displayio.Group()
display.root_group = splash

color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = BACKGROUND_COLOR

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(
    display.width - BORDER * 2, display.height - BORDER * 2, 1
)
inner_palette = displayio.Palette(1)
inner_palette[0] = FOREGROUND_COLOR
inner_sprite = displayio.TileGrid(
    inner_bitmap, pixel_shader=inner_palette, x=BORDER, y=BORDER
)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=TEXT_COLOR)
text_width = text_area.bounding_box[2] * FONTSCALE
text_group = displayio.Group(
    scale=FONTSCALE,
    x=display.width // 2 - text_width // 2,
    y=display.height // 2,
)
text_group.append(text_area)  # Subgroup for text scaling
splash.append(text_group)

circle = Circle(120, 75, 35, fill=0x704d08, outline=0x704d08)
splash.append(circle)

circle = Circle(111, 65, 6, fill=0xffffff, outline=0xffffff)
splash.append(circle)

circle = Circle(111, 67, 3, fill=0x030303, outline=0x030303)
splash.append(circle)

circle = Circle(129, 65, 6, fill=0xffffff, outline=0xffffff)
splash.append(circle)

circle = Circle(129, 67, 3, fill=0x030303, outline=0x030303)
splash.append(circle)

triangle = Triangle(115, 85, 125, 80, 120, 70, fill=0xfa9805, outline=0xfa9805)
splash.append(triangle)

roundrect = RoundRect(122, 79, 12, 20, 6, fill=0xcf3c1f, outline=0xcf3c1f, stroke=6)
splash.append(roundrect)

circle = Circle(120, 32, 10, fill=0xa87728, outline=0xa87728)
splash.append(circle)

circle = Circle(120, 27, 10, fill=0xa87728, outline=0xa87728)
splash.append(circle)

circle = Circle(120, 22, 10, fill=0xa87728, outline=0xa87728)
splash.append(circle)

circle = Circle(100, 40, 10, fill=0xc48114, outline=0xc48114)
splash.append(circle)

circle = Circle(95, 35, 10, fill=0xc48114, outline=0xc48114)
splash.append(circle)

circle = Circle(90, 30, 10, fill=0xc48114, outline=0xc48114)
splash.append(circle)

circle = Circle(140, 45, 10, fill=0xc48114, outline=0xc48114)
splash.append(circle)

circle = Circle(145, 40, 10, fill=0xc48114, outline=0xc48114)
splash.append(circle)

circle = Circle(150, 35, 10, fill=0xc48114, outline=0xc48114)
splash.append(circle)

circle = Circle(85, 60, 10, fill=0xa87728, outline=0xa87728)
splash.append(circle)

circle = Circle(80, 55, 10, fill=0xa87728, outline=0xa87728)
splash.append(circle)

circle = Circle(75, 50, 10, fill=0xa87728, outline=0xa87728)
splash.append(circle)

circle = Circle(152, 60, 10, fill=0xa87728, outline=0xa87728)
splash.append(circle)

circle = Circle(157, 55, 10, fill=0xa87728, outline=0xa87728)
splash.append(circle)

circle = Circle(162, 50, 10, fill=0xa87728, outline=0xa87728)
splash.append(circle)

while True:
    pass
