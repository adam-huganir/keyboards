import time

import board
import digitalio
from kmk.hid import HIDModes

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.keypad import MatrixScanner

import adafruit_ble

def make_keyboard():
    pass


class LilGuy(KMKKeyboard):
    col_pins = [board.IO1, board.IO2, board.IO3]
    row_pins = [board.IO4, board.IO5, board.IO6]
    # diode_orientation = DiodeOrientation.COL2ROW
    coord_mapping = [7, 0, 1, 2, 8, 3, 4, 5]

    def __init__(self):
        # create and register the scanner
        self.matrix = MatrixScanner(
            column_pins=self.col_pins,
            row_pins=self.row_pins,
        )


keyboard = LilGuy()
# fmt: off
keyboard.keymap = [
    [
        KC.F13, KC.F14, KC.F15, KC.F16,
        KC.F17, KC.F18, KC.F19, KC.F20,
    ],
    [
        KC.A, KC.B, KC.C, KC.D,
        KC.E, KC.F, KC.G, KC.H,
    ],
]
# fmt: on


encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.IO9, board.IO10, board.IO0),)
encoder_handler.map = [
    ((KC.UP, KC.DOWN, KC.MUTE),),
]

keyboard.modules.append(encoder_handler)

if __name__ == "__main__":
    keyboard.debug_enabled = True
    keyboard.go()
