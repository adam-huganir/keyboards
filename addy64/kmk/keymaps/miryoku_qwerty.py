# Copyright 2022 Manna Harbour
# github.com/manna-harbour/miryoku
# generated by and then tweaked by Adam Huganir <adam-huganir@github>


from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.capsword import CapsWord
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.power import Power
from kmk.modules.tapdance import TapDance


def apply(keyboard):
    keyboard.extensions.append(MediaKeys())
    keyboard.modules.append(CapsWord())
    keyboard.modules.append(Layers())
    keyboard.modules.append(ModTap())
    keyboard.modules.append(MouseKeys())
    keyboard.modules.append(Power())
    keyboard.modules.append(TapDance())
    # fmt: on
    _____ = KC.NO
    keyboard.keymap = [
        # BASE
        [
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.Q,
            KC.W,
            KC.E,
            KC.R,
            KC.T,
            KC.Y,
            KC.U,
            KC.I,
            KC.O,
            KC.P,
            _____,
            _____,
            KC.MT(KC.A, KC.LGUI),
            KC.MT(KC.S, KC.LALT),
            KC.MT(KC.D, KC.LCTL),
            KC.MT(KC.F, KC.LSFT),
            KC.G,
            KC.H,
            KC.MT(KC.J, KC.LSFT),
            KC.MT(KC.K, KC.LCTL),
            KC.MT(KC.L, KC.LALT),
            KC.MT(KC.QUOT, KC.LGUI),
            _____,
            _____,
            KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False),
            KC.MT(KC.X, KC.RALT),
            KC.C,
            KC.V,
            KC.B,
            _____,
            _____,
            KC.N,
            KC.M,
            KC.COMM,
            KC.MT(KC.DOT, KC.RALT),
            KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False),
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False),
            KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False),
            KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False),
            KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False),
            KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False),
            KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False),
            _____,
            _____,
            _____,
            _____,
        ],
        # EXTRA
        [
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.Q,
            KC.W,
            KC.E,
            KC.R,
            KC.T,
            KC.Y,
            KC.U,
            KC.I,
            KC.O,
            KC.P,
            _____,
            _____,
            KC.MT(KC.A, KC.LGUI),
            KC.MT(KC.S, KC.LALT),
            KC.MT(KC.D, KC.LCTL),
            KC.MT(KC.F, KC.LSFT),
            KC.G,
            KC.H,
            KC.MT(KC.J, KC.LSFT),
            KC.MT(KC.K, KC.LCTL),
            KC.MT(KC.L, KC.LALT),
            KC.MT(KC.QUOT, KC.LGUI),
            _____,
            _____,
            KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False),
            KC.MT(KC.X, KC.RALT),
            KC.C,
            KC.V,
            KC.B,
            _____,
            _____,
            KC.N,
            KC.M,
            KC.COMM,
            KC.MT(KC.DOT, KC.RALT),
            KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False),
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False),
            KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False),
            KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False),
            KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False),
            KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False),
            KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False),
            _____,
            _____,
            _____,
            _____,
        ],
        # TAP
        [
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.Q,
            KC.W,
            KC.F,
            KC.P,
            KC.B,
            KC.J,
            KC.L,
            KC.U,
            KC.Y,
            KC.QUOT,
            _____,
            _____,
            KC.A,
            KC.R,
            KC.S,
            KC.T,
            KC.G,
            KC.M,
            KC.N,
            KC.E,
            KC.I,
            KC.O,
            _____,
            _____,
            KC.Z,
            KC.X,
            KC.C,
            KC.D,
            KC.V,
            _____,
            _____,
            KC.K,
            KC.H,
            KC.COMM,
            KC.DOT,
            KC.SLSH,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.ESC,
            KC.SPC,
            KC.TAB,
            KC.ENT,
            KC.BSPC,
            KC.DEL,
            _____,
            _____,
            _____,
            _____,
        ],
        # BUTTON
        [
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.LSFT(KC.DEL),
            KC.LCTL(KC.INS),
            KC.LSFT(KC.INS),
            _____,
            _____,
            KC.LSFT(KC.INS),
            KC.LCTL(KC.INS),
            KC.LSFT(KC.DEL),
            _____,
            _____,
            _____,
            KC.LGUI,
            KC.LALT,
            KC.LCTL,
            KC.LSFT,
            _____,
            _____,
            KC.LSFT,
            KC.LCTL,
            KC.LALT,
            KC.LGUI,
            _____,
            _____,
            _____,
            KC.LSFT(KC.DEL),
            KC.LCTL(KC.INS),
            KC.LSFT(KC.INS),
            _____,
            _____,
            _____,
            _____,
            KC.LSFT(KC.INS),
            KC.LCTL(KC.INS),
            KC.LSFT(KC.DEL),
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.MB_MMB,
            KC.MB_LMB,
            KC.MB_RMB,
            KC.MB_RMB,
            KC.MB_LMB,
            KC.MB_MMB,
            _____,
            _____,
            _____,
            _____,
        ],
        # NAV
        [
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.TD(_____, KC.RELOAD),
            KC.TD(_____, KC.DF(2)),
            KC.TD(_____, KC.DF(1)),
            KC.TD(_____, KC.DF(0)),
            _____,
            _____,
            KC.LSFT(KC.INS),
            KC.LCTL(KC.INS),
            KC.LSFT(KC.DEL),
            _____,
            _____,
            _____,
            KC.LGUI,
            KC.LALT,
            KC.LCTL,
            KC.LSFT,
            _____,
            KC.LEFT,
            KC.DOWN,
            KC.UP,
            KC.RGHT,
            KC.TD(KC.CW, KC.CAPS),
            _____,
            _____,
            _____,
            KC.RALT,
            KC.TD(_____, KC.DF(7)),
            KC.TD(_____, KC.DF(4)),
            _____,
            _____,
            _____,
            KC.HOME,
            KC.PGDN,
            KC.PGUP,
            KC.END,
            KC.INS,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.ENT,
            KC.BSPC,
            KC.DEL,
            _____,
            _____,
            _____,
            _____,
        ],
        # MOUSE
        [
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.TD(_____, KC.RELOAD),
            KC.TD(_____, KC.DF(2)),
            KC.TD(_____, KC.DF(1)),
            KC.TD(_____, KC.DF(0)),
            _____,
            _____,
            KC.LSFT(KC.INS),
            KC.LCTL(KC.INS),
            KC.LSFT(KC.DEL),
            _____,
            _____,
            _____,
            KC.LGUI,
            KC.LALT,
            KC.LCTL,
            KC.LSFT,
            _____,
            KC.MS_LT,
            KC.MS_DN,
            KC.MS_UP,
            KC.MS_RT,
            _____,
            _____,
            _____,
            _____,
            KC.RALT,
            KC.TD(_____, KC.DF(8)),
            KC.TD(_____, KC.DF(5)),
            _____,
            _____,
            _____,
            _____,
            KC.MW_DN,
            KC.MW_UP,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.MB_RMB,
            KC.MB_LMB,
            KC.MB_MMB,
            _____,
            _____,
            _____,
            _____,
        ],
        # MEDIA
        [
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.TD(_____, KC.RELOAD),
            KC.TD(_____, KC.DF(2)),
            KC.TD(_____, KC.DF(1)),
            KC.TD(_____, KC.DF(0)),
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.LGUI,
            KC.LALT,
            KC.LCTL,
            KC.LSFT,
            _____,
            KC.MPRV,
            KC.VOLD,
            KC.VOLU,
            KC.MNXT,
            KC.PS_TOG,
            _____,
            _____,
            _____,
            KC.RALT,
            KC.TD(_____, KC.DF(9)),
            KC.TD(_____, KC.DF(6)),
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.HID,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.MSTP,
            KC.MPLY,
            KC.MUTE,
            _____,
            _____,
            _____,
            _____,
        ],
        # NUM
        [
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.LBRC,
            KC.N7,
            KC.N8,
            KC.N9,
            KC.RBRC,
            _____,
            KC.TD(_____, KC.DF(0)),
            KC.TD(_____, KC.DF(1)),
            KC.TD(_____, KC.DF(2)),
            KC.TD(_____, KC.RELOAD),
            _____,
            _____,
            KC.SCLN,
            KC.N4,
            KC.N5,
            KC.N6,
            KC.EQL,
            _____,
            KC.LSFT,
            KC.LCTL,
            KC.LALT,
            KC.LGUI,
            _____,
            _____,
            KC.GRV,
            KC.N1,
            KC.N2,
            KC.N3,
            KC.BSLS,
            _____,
            _____,
            _____,
            KC.TD(_____, KC.DF(7)),
            KC.TD(_____, KC.DF(4)),
            KC.RALT,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.DOT,
            KC.N0,
            KC.MINS,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
        ],
        # SYM
        [
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.LCBR,
            KC.AMPR,
            KC.ASTR,
            KC.LPRN,
            KC.RCBR,
            _____,
            KC.TD(_____, KC.DF(0)),
            KC.TD(_____, KC.DF(1)),
            KC.TD(_____, KC.DF(2)),
            KC.TD(_____, KC.RELOAD),
            _____,
            _____,
            KC.COLN,
            KC.DLR,
            KC.PERC,
            KC.CIRC,
            KC.PLUS,
            _____,
            KC.LSFT,
            KC.LCTL,
            KC.LALT,
            KC.LGUI,
            _____,
            _____,
            KC.TILD,
            KC.EXLM,
            KC.AT,
            KC.HASH,
            KC.PIPE,
            _____,
            _____,
            _____,
            KC.TD(_____, KC.DF(8)),
            KC.TD(_____, KC.DF(5)),
            KC.RALT,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.LPRN,
            KC.RPRN,
            KC.UNDS,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
        ],
        # FUN
        [
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.F12,
            KC.F7,
            KC.F8,
            KC.F9,
            KC.PSCR,
            _____,
            KC.TD(_____, KC.DF(0)),
            KC.TD(_____, KC.DF(1)),
            KC.TD(_____, KC.DF(2)),
            KC.TD(_____, KC.RELOAD),
            _____,
            _____,
            KC.F11,
            KC.F4,
            KC.F5,
            KC.F6,
            KC.SLCK,
            _____,
            KC.LSFT,
            KC.LCTL,
            KC.LALT,
            KC.LGUI,
            _____,
            _____,
            KC.F10,
            KC.F1,
            KC.F2,
            KC.F3,
            KC.PAUS,
            _____,
            _____,
            _____,
            KC.TD(_____, KC.DF(9)),
            KC.TD(_____, KC.DF(6)),
            KC.RALT,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            KC.APP,
            KC.SPC,
            KC.TAB,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
            _____,
        ],
    ]

    # fmt: on
    layer_names_list = [
        "Base",
        "Extra",
        "Tap",
        "Button",
        "Nav",
        "Mouse",
        "Media",
        "Num",
        "Sym",
        "Fun",
    ]
    return keyboard, layer_names_list
