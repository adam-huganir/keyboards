import adafruit_bitmap_font
import adafruit_ble

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


def kb_side():
    return "RIGHT" if str(getmount("/").label)[-1] == "R" else "LEFT"


side = kb_side()
print(f"Side: {side}")


class SplitAddy(KMKKeyboard):
    col_pins = (
        [
            board.P0_24,
            board.P0_17,
            board.P1_00,
            board.P1_04,
            board.P0_20,
            board.P0_22,
            board.P0_11,
        ]
        if kb_side() == "LEFT"
        else [
            board.P0_24,
            board.P0_11,
            board.P0_22,
            board.P0_20,
            board.P1_00,
            board.P0_17,
            board.P1_04,
        ]
    )
    row_pins = (
        [
            board.P1_11,
            board.P0_02,
            board.P1_15,
            board.P1_13,
            board.P0_10,
        ]
        if kb_side() == "LEFT"
        else [
            board.P1_11,
            board.P0_10,
            board.P1_13,
            board.P1_15,
            board.P0_02,
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
            0,  1,  2,  3,  4,  5,              36, 37, 38, 39, 40, 41,
            7,   8,  9, 10, 11, 12, 13,     42, 43, 44, 45, 46, 47, 48,
            14, 15, 16, 17, 18, 19, 20,     49, 50, 51, 52, 53, 54, 55,
            21, 22, 23, 24, 25, 26, 27,     56, 57, 58, 59, 60, 61, 62,
                    30, 31, 32, 33, 34,     63, 64, 65, 66, 67,
        ]
        # fmt: on


keyboard = SplitAddy()
keyboard.modules.append(HoldTap())


class AddySide(Split):
    def _check_all_connections(self, keyboard):
        """Validates the correct number of BLE connections"""
        self._previous_connection_count = self._connection_count
        self._connection_count = len(self._ble.connections)
        if self._is_target:
            if self._advertising or not self._check_if_split_connected():
                self._target_advertise()
            elif self._connection_count < 2 and keyboard.hid_type == HIDModes.BLE:
                keyboard._hid_helper.start_advertising()

        elif not self._is_target and self._connection_count < 1:
            self._initiator_scan()


split = AddySide(
    debug_enabled=True,
    split_type=SplitType.BLE,
    split_target_left=True,
    split_side=SplitSide.LEFT if side == "LEFT" else SplitSide.RIGHT,
)

_____ = KC.TRNS
xxxxx = KC.NO
# fmt: off
HT_A = KC.HT(KC.A, KC.LGUI)
HT_S = KC.HT(KC.S, KC.LCTL)
HT_D = KC.HT(KC.D, KC.LALT)
HT_F = KC.HT(KC.F, KC.LSFT)

HT_J = KC.HT(KC.J, KC.RSFT)
HT_K = KC.HT(KC.K, KC.RALT)
HT_L = KC.HT(KC.L, KC.RCTL)
HT_SCLN = KC.HT(KC.SCLN, KC.RGUI)

keyboard.keymap = [
    [
        KC.GRV,      KC.N1,       KC.N2,       KC.N3,       KC.N4,       KC.N5,                                 KC.N6,       KC.N7,       KC.N8,       KC.N9,       KC.N0,       KC.GRV,
        KC.TAB,      KC.Q,        KC.W,        KC.E,        KC.R,        KC.T,        KC.MINS,     KC.QUOT,     KC.Y,        KC.U,        KC.I,        KC.O,        KC.P,        KC.MINS,
        KC.LCTL,     HT_A,        HT_S,        HT_D,        HT_F,        KC.G,        KC.EQL,      KC.BSLS,     KC.H,        HT_J,        HT_K,        HT_L,        HT_SCLN,     KC.RCTL,
        KC.LSFT,     KC.Z,        KC.X,        KC.C,        KC.V,        KC.B,        KC.LBRC,     KC.RBRC,     KC.N,        KC.M,        KC.COMM,     KC.DOT,      KC.SLSH,     KC.RSFT,
                                  KC.SPC,      KC.ESC,      KC.SPC,      KC.TAB,      KC.ENTER,    KC.ESC,      KC.ENTER,    KC.BSPC,     KC.DEL,      KC.DEL,
    ]
]
# fmt: on

keyboard.modules.append(split)
keyboard.debug_enabled = True
if __name__ == "__main__":
    print(f"Starting keyboard {side}")
    keyboard.go(
        hid_type=HIDModes.BLE,
        ble_name="Addy64",
        # secondary_hid_type=HIDModes.USB,
    )
