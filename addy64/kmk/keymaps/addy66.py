try:
    from kmk.keys import KC
except ImportError:

    class _KC(object):
        """dummy for formatting"""

        def __getattr__(self, __name: str):
            if __name or __name in {"LT", "MT", "TD", "DF"}:
                return lambda *args, **kwargs: __name
            extra_symbols = {"NO": "xxxxx", "TRNS": "xxxxx"}
            return extra_symbols.get("__name", __name)

        def __getitem__(self, __name: str):
            return __name

    KC = _KC()


# noinspection PyPep8Naming
def apply(keyboard):  # sourcery skip: merge-dict-assign
    _____ = KC.TRNS
    xxxxx = KC.NO
    ooooo = KC.NO # THIS one is that there is no phsycical key



    tap_time = 300
    LT_3SLSH = KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
    LT_3Z = KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
    LT_4SPC = KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
    LT_5TAB = KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
    LT_6ESC = KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
    LT_7BSPC = KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
    LT_8ENT = KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
    LT_9DEL = KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
    MT_ALGUI = KC.MT(KC.A, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=tap_time)
    MT_DLCTL = KC.MT(KC.D, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=tap_time)
    MT_DOTRALT = KC.MT(KC.DOT, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time)
    MT_FLSFT = KC.MT(KC.F, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time)
    MT_JLSFT = KC.MT(KC.J, KC.LSFT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time)
    MT_KLCTL = KC.MT(KC.K, KC.LCTL, prefer_hold=False, tap_interrupted=True, tap_time=tap_time)
    MT_LLALT = KC.MT(KC.L, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time)
    MT_QUOTLGUI = KC.MT(KC.QUOT, KC.LGUI, prefer_hold=False, tap_interrupted=True, tap_time=tap_time)
    MT_SLALT = KC.MT(KC.S, KC.LALT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time)
    MT_XRALT = KC.MT(KC.X, KC.RALT, prefer_hold=False, tap_interrupted=True, tap_time=tap_time)
    TD_CWCAPS = KC.TD(KC.CW, KC.CAPS, tap_time=tap_time)
    TD_NODF0 = KC.TD(_____, KC.DF(0), tap_time=tap_time)
    TD_NODF1 = KC.TD(_____, KC.DF(1), tap_time=tap_time)
    TD_NODF2 = KC.TD(_____, KC.DF(2), tap_time=tap_time)
    TD_NODF4 = KC.TD(_____, KC.DF(4), tap_time=tap_time)
    TD_NODF5 = KC.TD(_____, KC.DF(5), tap_time=tap_time)
    TD_NODF6 = KC.TD(_____, KC.DF(6), tap_time=tap_time)
    TD_NODF7 = KC.TD(_____, KC.DF(7), tap_time=tap_time)
    TD_NODF8 = KC.TD(_____, KC.DF(8), tap_time=tap_time)
    TD_NODF9 = KC.TD(_____, KC.DF(9), tap_time=tap_time)
    TD_NORELOAD = KC.TD(_____, KC.RELOAD, tap_time=tap_time)

    # fmt: off
    mapping = {}
    mapping["Base"] = [
        KC.GRV,      KC.N1,       KC.N2,       KC.N3,       KC.N4,       KC.N5,       ooooo,       ooooo,       KC.N6,       KC.N7,       KC.N8,       KC.N9,       KC.N0,       KC.GRV,
        KC.TAB,      KC.Q,        KC.W,        KC.E,        KC.R,        KC.T,        KC.SLSH,       xxxxx,       KC.Y,        KC.U,        KC.I,        KC.O,        KC.P,        KC.MINS,
        KC.LCTL,     MT_ALGUI,    MT_SLALT,    MT_DLCTL,    MT_FLSFT,    KC.G,        KC.DOT,       xxxxx,       KC.H,        MT_JLSFT,    MT_KLCTL,    MT_LLALT,    MT_QUOTLGUI, KC.COLN,
        KC.LSFT,     LT_3Z,       MT_XRALT,    KC.C,        KC.V,        KC.B,        KC.LBRC,     KC.RBRC,     KC.N,        KC.M,        KC.COMM,     MT_DOTRALT,  LT_3SLSH,    KC.RSFT,
        ooooo,       ooooo,       KC.ESC,      LT_6ESC,     LT_4SPC,     LT_5TAB,     KC.ENTER,    KC.F,        LT_8ENT,     LT_7BSPC,    LT_9DEL,     KC.Q,        ooooo,       ooooo,
    ]
    mapping["Extra"] = [
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       ooooo,       ooooo,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
        xxxxx,       KC.Q,        KC.W,        KC.E,        KC.R,        KC.T,        xxxxx,       xxxxx,       KC.Y,        KC.U,        KC.I,        KC.O,        KC.P,        xxxxx,
        xxxxx,       MT_ALGUI,    MT_SLALT,    MT_DLCTL,    MT_FLSFT,    KC.G,        xxxxx,       xxxxx,       KC.H,        MT_JLSFT,    MT_KLCTL,    MT_LLALT,    MT_QUOTLGUI, xxxxx,
        xxxxx,       LT_3Z,       MT_XRALT,    KC.C,        KC.V,        KC.B,        xxxxx,       xxxxx,       KC.N,        KC.M,        KC.COMM,     MT_DOTRALT,  LT_3SLSH,    xxxxx,
        ooooo,       ooooo,       KC.ESC,      LT_6ESC,     LT_4SPC,     LT_5TAB,     xxxxx,       xxxxx,       LT_8ENT,     LT_7BSPC,    LT_9DEL,     xxxxx,       ooooo,       ooooo,
    ]
    mapping["Tap"] = [
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
        xxxxx,       KC.Q,        KC.W,        KC.F,        KC.P,        KC.B,        xxxxx,       xxxxx,       KC.J,        KC.L,        KC.U,        KC.Y,        KC.QUOT,     xxxxx,
        xxxxx,       KC.A,        KC.R,        KC.S,        KC.T,        KC.G,        xxxxx,       xxxxx,       KC.M,        KC.N,        KC.E,        KC.I,        KC.O,        xxxxx,
        xxxxx,       KC.Z,        KC.X,        KC.C,        KC.D,        KC.V,        xxxxx,       xxxxx,       KC.K,        KC.H,        KC.COMM,     KC.DOT,      KC.SLSH,     xxxxx,
        ooooo,       ooooo,       KC.ESC,      KC.ESC,      KC.SPC,      KC.TAB,      xxxxx,       xxxxx,       KC.ENT,      KC.BSPC,     KC.DEL,      xxxxx,       ooooo,       ooooo,
    ]
    mapping["Button"] = [
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
        xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,
        xxxxx,       KC.LGUI,     KC.LALT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LALT,     KC.LGUI,     xxxxx,
        xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,
        xxxxx,       xxxxx,       KC.ESC,      KC.MB_MMB,   KC.MB_LMB,   KC.MB_RMB,   xxxxx,       xxxxx,       KC.MB_RMB,   KC.MB_LMB,   KC.MB_MMB,   xxxxx,       xxxxx,       xxxxx,
    ]
    mapping["Nav"] = [
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
        xxxxx,       TD_NORELOAD, TD_NODF2,    TD_NODF1,    TD_NODF0,    xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,
        xxxxx,       KC.LGUI,     KC.LALT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       TD_CWCAPS,   KC.LEFT,     KC.DOWN,     KC.UP,       KC.RGHT,     xxxxx,
        xxxxx,       xxxxx,       KC.RALT,     TD_NODF7,    TD_NODF4,    xxxxx,       xxxxx,       xxxxx,       KC.INS,      KC.HOME,     KC.PGDN,     KC.PGUP,     KC.END,      xxxxx,
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.ENT,      KC.BSPC,     KC.DEL,      xxxxx,       xxxxx,       xxxxx,       xxxxx,
    ]
    mapping["Mouse"] = [
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
        xxxxx,       TD_NORELOAD, TD_NODF2,    TD_NODF1,    TD_NODF0,    xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,
        xxxxx,       KC.LGUI,     KC.LALT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.MS_LT,    KC.MS_DN,    KC.MS_UP,    KC.MS_RT,    xxxxx,
        xxxxx,       xxxxx,       KC.RALT,     TD_NODF8,    TD_NODF5,    xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.MW_DN,    KC.MW_UP,    xxxxx,       xxxxx,
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.MB_RMB,   KC.MB_LMB,   KC.MB_MMB,   xxxxx,       xxxxx,       xxxxx,       xxxxx,
    ]
    mapping["Media"] = [
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
        xxxxx,       TD_NORELOAD, TD_NODF2,    TD_NODF1,    TD_NODF0,    xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
        xxxxx,       KC.LGUI,     KC.LALT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       KC.PS_TOG,   KC.MPRV,     KC.VOLD,     KC.VOLU,     KC.MNXT,     xxxxx,
        xxxxx,       xxxxx,       KC.RALT,     TD_NODF9,    TD_NODF6,    xxxxx,       xxxxx,       xxxxx,       KC.HID,      xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.MSTP,     KC.MPLY,     KC.MUTE,     xxxxx,       xxxxx,       xxxxx,       xxxxx,
    ]
    mapping["Num"] = [
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
        xxxxx,       KC.LBRC,     KC.N7,       KC.N8,       KC.N9,       KC.RBRC,     xxxxx,       xxxxx,       xxxxx,       TD_NODF0,    TD_NODF1,    TD_NODF2,    TD_NORELOAD, xxxxx,
        xxxxx,       KC.SCLN,     KC.N4,       KC.N5,       KC.N6,       KC.EQL,      xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LALT,     KC.LGUI,     xxxxx,
        xxxxx,       KC.GRV,      KC.N1,       KC.N2,       KC.N3,       KC.BSLS,     xxxxx,       xxxxx,       xxxxx,       TD_NODF7,    TD_NODF4,    KC.RALT,     xxxxx,       xxxxx,
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.DOT,      KC.N0,       KC.MINS,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    ]
    mapping["Sym"] = [
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
        xxxxx,       KC.LCBR,     KC.AMPR,     KC.ASTR,     KC.LPRN,     KC.RCBR,     xxxxx,       xxxxx,       xxxxx,       TD_NODF0,    TD_NODF1,    TD_NODF2,    TD_NORELOAD, xxxxx,
        xxxxx,       KC.COLN,     KC.DLR,      KC.PERC,     KC.CIRC,     KC.PLUS,     xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LALT,     KC.LGUI,     xxxxx,
        xxxxx,       KC.TILD,     KC.EXLM,     KC.AT,       KC.HASH,     KC.PIPE,     xxxxx,       xxxxx,       xxxxx,       TD_NODF8,    TD_NODF5,    KC.RALT,     xxxxx,       xxxxx,
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.LPRN,     KC.RPRN,     KC.UNDS,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    ]
    mapping["Fun"] = [
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
        xxxxx,       KC.F12,      KC.F7,       KC.F8,       KC.F9,       KC.PSCR,     xxxxx,       xxxxx,       xxxxx,       TD_NODF0,    TD_NODF1,    TD_NODF2,    TD_NORELOAD, xxxxx,
        xxxxx,       KC.F11,      KC.F4,       KC.F5,       KC.F6,       KC.SLCK,     xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LALT,     KC.LGUI,     xxxxx,
        xxxxx,       KC.F10,      KC.F1,       KC.F2,       KC.F3,       KC.PAUS,     xxxxx,       xxxxx,       xxxxx,       TD_NODF9,    TD_NODF6,    KC.RALT,     xxxxx,       xxxxx,
        xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.APP,      KC.SPC,      KC.TAB,      xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
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
    sorted_layers = sorted(mapping.items(), key=lambda item: layer_names_list.index(item[0]))
    print("Sorted layers: ", [s[0] for s in sorted_layers])
    keyboard.keymap = [s[1] for s in sorted_layers]
    keyboard.keymap_names = [s[0] for s in sorted_layers]
    print("Layers: ", keyboard.keymap_names)
    return keyboard, list(mapping)


if __name__ == "__main__":
    import inspect
    import re

    print("Pretty formatting...")

    current_block = None
    out = {}
    extract = False
    key_width = 14
    for line in inspect.getsourcelines(apply)[0]:
        if a := re.search(r'mapping\["(?P<name>\w+)"\]', line):
            current_block = a["name"]
            out[current_block] = []
            extract = True
            continue
        if line.strip() == "]":
            extract = False
        if extract:
            keys = re.findall(r"([\w\(\)\.]+),(?:\s{1,}|\n)", line)
            if len(keys) != key_width:
                for idx, k in enumerate(keys):
                    print(idx, k)
                raise ValueError(f"Wrong number of keys in {current_block} on line {len(out[current_block]) // key_width}")
            out[current_block].extend(keys)
    w = 13
    for key in out:
        to_format = [f"{k}," for k in out[key]]
        print(f'    mapping["{key}"] = [')
        print(((" " * 8 + (f"{{:{w}}}" * key_width + "\n")) * 5).format(*to_format), end="")
        print("    ]")

