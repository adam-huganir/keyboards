import board
import busio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from displayio import Bitmap
from oled import CustomOled
from storage import getmount

from kmk.extensions.media_keys import MediaKeys
from kmk.modules.split import
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.capsword import CapsWord
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.pimoroni_trackball import Trackball, TrackballMode
from kmk.modules.power import Power
from kmk.modules.split import Split, SplitType
from kmk.modules.tapdance import TapDance
from kmk.scanners import DiodeOrientation
from kmk.scanners.keypad import MatrixScanner

import keymap


def kb_side():
    return "RIGHT" if str(getmount("/").label)[-1] == "R" else "LEFT"

print(dir(board))
class SplitAddy(KMKKeyboard):
    col_pins = (
        [
            board.P0_24,
            board.P0_11,
            board.P0_22,
            board.P0_20,
            board.P1_00,
            board.P0_17,
            board.P1_04,
        ]
        if kb_side() == "LEFT"
        else [
            board.P0_24,
            board.P0_17,
            board.P1_00,
            board.P1_04,
            board.P0_20,
            board.P0_22,
            board.P0_11,
        ]
    )
    row_pins = (
        [
            board.P1_11,
            board.P0_10,
            board.P1_13,
            board.P1_15,
            board.P0_02,
        ]
        if kb_side() == "LEFT"
        else [
            board.P1_11,
            board.P0_02,
            board.P1_15,
            board.P1_13,
            board.P0_10,
        ]
    )
    diode_orientation = DiodeOrientation.COL2ROW

    def __init__(self):
        self.matrix = MatrixScanner(
            row_pins=self.row_pins,
            column_pins=self.col_pins,
            columns_to_anodes=self.diode_orientation,
        )


keyboard = SplitAddy()

split = Split(
    split_target_left=False,
    split_type=SplitType.BLE
    )


keyboard.modules.append(split)
# keyboard.modules.append(encoder_handler)
keyboard.modules.append(CapsWord())
keyboard.modules.append(Layers())
keyboard.modules.append(MouseKeys())
keyboard.modules.append(Power())
keyboard.modules.append(TapDance())
keyboard.extensions.append(MediaKeys())


keymap.configure(keyboard)

if kb_side() == "LEFT":

    def view1(self, layer):
        text = self.returnCurrectRenderText(layer, self._views[0])
        x_offset = int(self._font_weight_avg * len(text) // 2)
        scale = 1
        x = self._width // 2 - int(self._font_weight_avg * scale * len(text) // 2)
        header_px = 8
        v_center = header_px + (self._height - header_px) // 2
        return label.Label(self._font, text=text, color=0xFFFFFF, x=x, y=v_center, scale=scale)

    print("attempting to load oled display on  on the right side")
    try:
        font = bitmap_font.load_font("./font.bdf", Bitmap)
    except OSError:
        print("font not found, using terminalio font")
        font = None
    layers = keyboard.keymap_names + ["?"] * 2  # give some padding
    layer_ints = [str(i) for i in range(len(layers))]
    try:
        oled = CustomOled(
            views=[
                {0: view1, 1: layers},
            ],
            i2c=busio.I2C(board.P0_06, board.P0_08),
            oWidth=128,
            oHeight=64,
            flip=False,
            font=font,
        )
        keyboard.extensions.append(oled)
    except RuntimeError:
        print("oled display not found, skipping")
else:
    try:
        trackball = Trackball(
            busio.I2C(board.P0_06, board.P0_08),
            mode=TrackballMode.MOUSE_MODE,
            angle_offset=185,
        )
        trackball.set_rgbw(50, 0, 60, 60)  # Set the RGBW LED to a dim white
        keyboard.modules.append(trackball)
    except RuntimeError:
        print("trackball not found, skipping")
