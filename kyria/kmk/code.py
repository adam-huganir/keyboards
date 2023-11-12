import adafruit_bitmap_font

# Just to make sure circup keeps this installed
import adafruit_display_text  # noqa
import adafruit_displayio_ssd1306
import board
from kmk.hid import HIDModes
from storage import getmount

from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.holdtap import HoldTap
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
import myk as keymap


def kb_side():
    return "RIGHT" if str(getmount("/").label)[-1] == "R" else "LEFT"


side = kb_side()
print(f"Side: {side}")


class SplitAddy(KMKKeyboard):
    col_pins = (
        [
            board.D2,
            board.D3,
            board.D4,
            board.D5,
            board.D6,
            board.D7,
        ]
        if kb_side() == "LEFT"
        else [
            board.D2,
            board.D3,
            board.D4,
            board.D5,
            board.D6,
            board.D7,
        ]
    )
    row_pins = (
        [
            board.SCK,
            board.MISO,
            board.MOSI,
            board.D10,
        ]
        if kb_side() == "LEFT"
        else [
            board.D10,
            board.MOSI,
            board.MISO,
            board.SCK,
        ]
    )
    diode_orientation = DiodeOrientation.COL2ROW

    def __init__(self):
        self.matrix = MatrixScanner(
            row_pins=self.row_pins,
            column_pins=self.col_pins,
            columns_to_anodes=self.diode_orientation,
        )
        # fmt: off
        # coords = """self.coord_mapping = [
        # {:2}, {:2}, {:2}, {:2}, {:2}, {:2},         {:2}, {:2}, {:2}, {:2}, {:2}, {:2},
        # {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2},
        # {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2},
        # {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2},
        #         {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2}, {:2},
        # ]""".format(
        #     *range(0,6),     *range(32, 38),
        #     *range(6, 13),   *range(38, 45),
        #     *range(13, 20),  *range(45, 52),
        #     *range(20, 27),  *range(52, 59),
        #     *range(27, 32),  *range(59, 64),
        # )
        self.coord_mapping = [
            0,  1,  2,  3,  4,  5,                     24, 25, 26, 27, 28, 29,
            6,  7,  8,  9,  10, 11,                    30, 31, 32, 33, 34, 35,
            12, 13, 14, 15, 16, 17,    23,    42, 43,  36, 37, 38, 39, 40, 41,
                       18, 19, 20, 21, 22,        44, 45, 46, 47
        ]
        # fmt: on


keyboard = SplitAddy()
split = Split(
    debug_enabled=True,
    split_target_left=True,
    use_pio=True,
    data_pin=board.D0,
)
_ = keymap.configure(keyboard)


keyboard.modules.append(split)
keyboard.debug_enabled = True
if __name__ == "__main__":
    print(f"Starting keyboard {side}")
    keyboard.go()
