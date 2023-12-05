import adafruit_bitmap_font

# Just to make sure circup keeps this installed
import adafruit_display_text  # noqa
import adafruit_displayio_ssd1306  # noqa
import board
from storage import getmount
from kmk.modules.pimoroni_trackball import Trackball, TrackballMode

from kmk.keys import KC
from kmk.extensions.peg_oled_Display import Oled, OledDisplayMode, OledReactionType, OledData

from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.holdtap import HoldTap
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner
import keymap

from kmk.extensions.media_keys import MediaKeys

from kmk.modules.capsword import CapsWord
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.power import Power
from kmk.modules.tapdance import TapDance
from kmk.modules.holdtap import HoldTap


def kb_side():
    return "RIGHT" if str(getmount("/").label)[-1] == "R" else "LEFT"


side = kb_side()
print(f"Side: {side}")


class Gudnuf(KMKKeyboard):
    col_pins = (
        [
            board.D5,
            board.D6,
            board.D7,
            board.D8,
            board.D9,
        ]
        if kb_side() == "LEFT"
        else [
            board.D5,
            board.D6,
            board.D7,
            board.D8,
            board.D9,
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
            board.A0,
            board.SCK,
            board.MISO,
            board.MOSI,
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
        #     *range(0,5),     *range(20, 25),
        #     *range(5, 10),   *range(25, 30),
        #     *range(10, 15),  *range(30, 35),
        #     *range(15, 20),  *range(35, 40),
        # )
        self.coord_mapping = [
            0,  1,   2,  3,  4,             20, 21, 22, 23, 24,
            5,  6,   7,  8,  9,             25, 26, 27, 28, 29,
            10, 11, 12, 13, 14, 19,     35, 30, 31, 32, 33, 34,
                    15, 16, 17, 18,     36, 37, 38, 39,
        ]
        # fmt: on


keyboard = Gudnuf()
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Power())
keyboard.modules.append(TapDance())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(CapsWord())
keyboard.modules.append(HoldTap())


split = Split(
    debug_enabled=True,
    split_target_left=False,
    use_pio=True,
    data_pin=board.D2,
)
_ = keymap.configure(keyboard)

if side == "LEFT":
    import displayio, gc

    class CustomOled(Oled):
        def __init__(self, views, toDisplay=OledDisplayMode.TXT, oWidth=128, oHeight=32, flip=False):
            displayio.release_displays()
            self.rotation = 180 if flip else 0
            self._views = views.data
            self._toDisplay = toDisplay
            self._width = oWidth
            self._height = oHeight
            self._prevLayers = 0
            gc.collect()

        def during_bootup(self, keyboard):
            B = keyboard
            displayio.release_displays()
            C = board.STEMMA_I2C()
            self._display = adafruit_displayio_ssd1306.SSD1306(
                displayio.I2CDisplay(C, device_address=60),
                width=self._width,
                height=self._height,
                rotation=self.rotation,
            )
            if self._toDisplay == OledDisplayMode.TXT:
                self.renderOledTextLayer(0)
            if self._toDisplay == OledDisplayMode.IMG:
                self.renderOledImgLayer(0)

    oled_ext = CustomOled(
        OledData(
            corner_one={0: OledReactionType.STATIC, 1: ["layer"]},
            corner_two={0: OledReactionType.LAYER, 1: ["1", "2", "3", "4"]},
            corner_three={0: OledReactionType.LAYER, 1: ["base", "raise", "lower", "adjust"]},
            corner_four={0: OledReactionType.LAYER, 1: ["qwerty", "nums", "shifted", "leds"]},
        ),
        toDisplay=OledDisplayMode.TXT,
        flip=False,
    )
    keyboard.extensions.append(oled_ext)
else:
    trackball = Trackball(
        board.STEMMA_I2C(),
        angle_offset=170,
    )
    keyboard.modules.append(trackball)

keyboard.modules.append(split)
keyboard.debug_enabled = True
if __name__ == "__main__":
    print(f"Starting keyboard {side}")
    keyboard.go()
