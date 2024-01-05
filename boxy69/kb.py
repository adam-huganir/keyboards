import board

from kmk.extensions.media_keys import MediaKeys
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.modules.capsword import CapsWord
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.power import Power
from kmk.modules.tapdance import TapDance
from kmk.scanners import DiodeOrientation


class OLKB(KMKKeyboard):
    col_pins = [
        board.D1,
        board.A3,
        board.A2,
        board.A1,
        board.A0,
        board.SCK,
        board.MISO,
        board.MOSI,
        board.D10,
    ]
    row_pins = [
        board.D2,
        board.D3,
        board.D4,
        board.D5,
        board.D6,
        board.D7,
        board.D8,
        board.D9,
    ]
    diode_orientation = DiodeOrientation.ROW2COL

    # fmt: off
    coord_mapping = (
        49, 50, 51, 52, 53, 0, 1, 2, 3, 4, 5, 6, 7, 8,
        48, 57, 58, 59, 60, 9, 10, 11, 12, 13, 14, 15, 16, 17,
        47, 56, 68, 69, 61, 18, 19, 20, 21, 22, 23, 24, 25, 26,
        46, 55, 67, 70, 62, 27, 28, 29, 30, 31, 32, 33, 34, 35,
        45, 54, 66, 71, 36, 37, 38, 39, 40, 41, 42, 43, 44,
    )
    # fmt: on

    def __init__(self):
        self.matrix = MatrixScanner(
            row_pins=self.row_pins,
            column_pins=self.col_pins,
            columns_to_anodes=self.diode_orientation,
        )


keyboard = OLKB()


import keymaps # noqa: E402S
print(dir(keymaps))
layer_names = keymaps.apply_keymap(keyboard)

