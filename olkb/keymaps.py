from kmk.extensions.media_keys import MediaKeys
from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.capsword import CapsWord
from kmk.modules.layers import Layers
from kmk.modules.mouse_keys import MouseKeys
from kmk.modules.tapdance import TapDance
from kmk.modules.holdtap import HoldTap

from kmk.keys import KC


# Layers
LBAS = 0
LMED = 1
LNAV = 2
LMOU = 3
LSYM = 4
LNUM = 5
LFUN = 6

K = KC
XXX = K.NO
___ = K.TRNS


def apply_keymap(keyboard: KMKKeyboard):
    # make sure our key extension modules are loaded
    MODULES = (CapsWord(), Layers(), MouseKeys(), HoldTap(), TapDance())
    EXTENSIONS = (MediaKeys(),)
    keyboard.modules.extend(MODULES)
    keyboard.extensions.extend(EXTENSIONS)

    # Homerow mods
    A_SUP = K.HT(K.A, K.LSUP)
    R_ALT = K.HT(K.R, K.LALT)
    S_CTL = K.HT(K.S, K.LCTL)
    T_SFT = K.HT(K.T, K.LSFT)
    N_SFT = K.HT(K.N, K.RSFT)
    E_CTL = K.HT(K.E, K.RCTL)
    I_ALT = K.HT(K.I, K.RALT)
    O_SUP = K.HT(K.O, K.RSUP)

    # Thumbs
    SPC_NAV = K.LT(LBAS, K.SPC)
    ESC_MED = K.LT(LMED, K.ESC)
    TAB_MOU = K.LT(LMOU, K.TAB)
    ENT_SYM = K.LT(LSYM, K.ENT)
    BSPC_NUM = K.LT(LNUM, K.BSPC)
    DEL_FUN = K.LT(LFUN, K.DEL)

    # mod shortcuts
    SH = K.SHIFT


    layers = ["base", "media", "nav", "mouse", "symbol", "number", "function"]
    # fmt: off
    KEYMAPS = {
        "base":
    [
    K.ESC,    K.N1,     K.N2,     K.N3,     K.N4,     K.N5,     K.HOME,   K.N6,     K.N7,     K.N8,     K.N9,     K.N0,     XXX,        XXX,
    K.TAB,    K.Q,      K.W,      K.F,      K.P,      K.B,      K.PGUP,   K.J,      K.L,      K.U,      K.Y,      K.QUOT,   XXX,        XXX,
    K.CAPS,   A_SUP,  R_ALT,    S_CTL,    T_SFT,      K.G,      K.PGDN,   K.M,      N_SFT,    E_CTL,    I_ALT,    O_SUP,    XXX,        XXX,
    K.LSFT,   K.Z,      K.X,      K.C,      K.D,      K.V,      K.END,    K.K,      K.H,      K.COMM,   K.DOT,    K.SLSH,   XXX,        XXX,
        K.LCTL,   K.LGUI,    K.LALT, ESC_MED, SPC_NAV,   TAB_MOU,   ENT_SYM, BSPC_NUM, DEL_FUN,    K.RALT,  K.RWIN,   K.RCTL,           XXX,
    ],
        "media":
    [
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      K.LGUI,   K.LALT,   K.LCTL,   K.LSFT,   XXX,      XXX,      XXX,      K.MPRV,   K.VOLU,   K.VOLD,   K.MNXT,   XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
         XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      K.MSTP,  K.PLY,   K.MUTE,      XXX,      XXX,          XXX,
    ],
        "nav":
    [
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      K.LGUI,   K.LALT,   K.LCTL,   K.LSFT,   XXX,      XXX,      K.CAPS,   K.LEFT,   K.DOWN,   K.UP,     K.RGHT,   XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      K.INS,    K.HOME,   K.PGDN,   K.PGUP,   K.END,    XXX,      XXX,
         XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      K.ENT,   K.BSPC,   K.DEL,    XXX,      XXX,      XXX,      XXX,
    ],
        "mouse":
    [
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      K.LGUI,   K.LALT,   K.LCTL,   K.LSFT,   XXX,      XXX,      XXX,      K.MS_LT,  K.MS_DN,  K.MS_UP,  K.MS_RT,  XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      K.MW_LT,  K.MW_DN,  K.MW_UP,  K.MW_RT,  XXX,      XXX,
         XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      K.MB_RMB, K.MB_LMB, K.MB_MMB,  XXX,      XXX,      XXX,      XXX,
    ],
        "symbol":
    [
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,   K.LABK,   K.RABK,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,   K.LPRN,   K.RPRN,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,   K.LBRC,   K.RBRC,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
         XXX,      XXX,      XXX,      K.LCBR,   K.RCBR,   XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    ],
        "number":
    [
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
         XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    ],
        "function":
    [
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
         XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,      XXX,
    ],
    }
    # fmt: on

    keyboard.keymap = [KEYMAPS[ln] for ln in layers]

    return layers
