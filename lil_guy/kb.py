import time

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import MatrixScanner, DiodeOrientation
from kmk.modules.encoder import EncoderHandler, GPIOEncoder
from kmk.extensions.media_keys import MediaKeys

# sleep for 10 seconds to let the esp32 finish booting before grabbing HID control
time.sleep(10)


class LilGuy(KMKKeyboard):
    row_pins = [
        board.IO1,
        board.IO2,
        board.IO3,
    ]
    col_pins = [
        board.IO4,
        board.IO5,
        board.IO6,
    ]

    diode_orientation = DiodeOrientation.COL2ROW

    def __init__(self):
        self.matrix = MatrixScanner(
            self.row_pins,
            self.col_pins,
        )


keyboard = LilGuy()
keyboard.extensions.append(MediaKeys())

# fmt: off
keyboard.keymap = [
    [
        KC.VOLD,     KC.VOLU,     KC.MUTE,
        KC.F13,      KC.F14,      KC.F15,
        KC.F16,      KC.F17,      KC.F18,
    ]
]
# fmt: on

encoder = EncoderHandler()
encoder.pins = [[board.IO8, board.IO9, None]]
encoder.map = [[(KC.VOLD, KC.VOLU, None)]]
keyboard.modules.extend((encoder,))
