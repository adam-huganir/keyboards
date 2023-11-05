from kmk.keys import KC
from keydef import get_definitions


# noinspection PyPep8Naming
def configure(keyboard):
    _____ = KC.TRNS
    xxxxx = KC.NO
    ooooo = KC.NO  # THIS one is that there is no phsycical key

    tap_time = 300
    # KD = get_definitions(tap_time)

    # fmt: off
    mapping = {}
    mapping["Base"] = [
        KC.GRV,      KC.N1,       KC.N2,       KC.N3,       KC.N4,       KC.N5,       xxxxx,       xxxxx,       KC.N6,       KC.N7,       KC.N8,       KC.N9,       KC.N0,       KC.GRV,
        KC.TAB,      KC.Q,        KC.W,        KC.E,        KC.R,        KC.T,        KC.MINS,     KC.QUOT,     KC.Y,        KC.U,        KC.I,        KC.O,        KC.P,        KC.MINS,
        KC.LCTL,     KC.A,        KC.S,        KC.D,        KC.F,        KC.G,        KC.EQL,      KC.BSLS,     KC.H,        KC.J,        KC.K,        KC.L,        KC.COLN,     KC.RCTL,
        KC.LSFT,     KC.Z,        KC.X,        KC.C,        KC.V,        KC.B,        KC.LBRC,     KC.RBRC,     KC.N,        KC.M,        KC.COMM,     KC.DOT,      KC.SLSH,     KC.RSFT,
        xxxxx,       xxxxx,       KC.SPC,      KC.ESC,      KC.SPC,      KC.TAB,      KC.ENTER,    KC.ESC,      KC.ENTER,    KC.BSPC,     KC.DEL,      KC.DEL,      xxxxx,       xxxxx,
    ]
    # mapping["Base"] = [
    #     KC.GRV,      KC.N1,       KC.N2,       KC.N3,       KC.N4,       KC.N5,       ooooo,       ooooo,       KC.N6,       KC.N7,       KC.N8,       KC.N9,       KC.N0,       KC.GRV,
    #     KC.TAB,      KC.Q,        KC.W,        KC.F,        KC.P,        KC.B,        KC.MINS,     KC.QUOT,     KC.J,        KC.L,        KC.U,        KC.Y,        KC.COLN,     KC.MINS,
    #     KC.LCTL,     KD.MT_ALGUI,    KD.MT_SLALT,    KD.MT_SLCTL,    KD.MT_TLSFT,    KC.G,        KC.EQL,      KC.BSLS,     KC.M,        KD.MT_NLSFT,    KD.MT_ELCTL,    KD.MT_ILALT,    KD.MT_OLGUI,    KC.COLN,
    #     KC.LSFT,     KD.LT_3Z,       KD.MT_XRALT,    KC.C,        KC.D,        KC.V,        KC.LBRC,     KC.RBRC,     KC.K,        KC.H,        KC.COMM,     KD.MT_DOTRALT,  KD.LT_3SLSH,    KC.RSFT,
    #     ooooo,       ooooo,       KC.ESC,      KD.LT_6ESC,     KD.LT_4SPC,     KD.LT_5TAB,     KC.ENTER,    KC.ESC,      KD.LT_8ENT,     KD.LT_7BSPC,    KD.LT_9DEL,     KC.Q,        ooooo,       ooooo,
    # ]
    # mapping["Extra"] = [
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       ooooo,       ooooo,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    #     xxxxx,       KC.Q,        KC.W,        KC.E,        KC.R,        KC.T,        xxxxx,       xxxxx,       KC.Y,        KC.U,        KC.I,        KC.O,        KC.P,        xxxxx,
    #     xxxxx,       KD.MT_ALGUI,    KD.MT_SLALT,    KD.MT_SLCTL,    KD.MT_TLSFT,    KC.G,        xxxxx,       xxxxx,       KC.H,        KD.MT_NLSFT,    KD.MT_ELCTL,    KD.MT_ILALT,    KD.MT_OLGUI,    xxxxx,
    #     xxxxx,       KD.LT_3Z,       KD.MT_XRALT,    KC.C,        KC.V,        KC.B,        xxxxx,       xxxxx,       KC.N,        KC.M,        KC.COMM,     KD.MT_DOTRALT,  KD.LT_3SLSH,    xxxxx,
    #     ooooo,       ooooo,       KC.ESC,      KD.LT_6ESC,     KD.LT_4SPC,     KD.LT_5TAB,     xxxxx,       xxxxx,       KD.LT_8ENT,     KD.LT_7BSPC,    KD.LT_9DEL,     xxxxx,       ooooo,       ooooo,
    # ]
    # mapping["Tap"] = [
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    #     xxxxx,       KC.Q,        KC.W,        KC.F,        KC.P,        KC.B,        xxxxx,       xxxxx,       KC.J,        KC.L,        KC.U,        KC.Y,        KC.QUOT,     xxxxx,
    #     xxxxx,       KC.A,        KC.R,        KC.R,        KC.T,        KC.G,        xxxxx,       xxxxx,       KC.M,        KC.N,        KC.E,        KC.I,        KC.O,        xxxxx,
    #     xxxxx,       KC.Z,        KC.X,        KC.C,        KC.S,        KC.V,        xxxxx,       xxxxx,       KC.K,        KC.H,        KC.COMM,     KC.DOT,      KC.SLSH,     xxxxx,
    #     ooooo,       ooooo,       KC.ESC,      KC.ESC,      KC.SPC,      KC.TAB,      xxxxx,       xxxxx,       KC.ENT,      KC.BSPC,     KC.DEL,      xxxxx,       ooooo,       ooooo,
    # ]
    # mapping["Button"] = [
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    #     xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,
    #     xxxxx,       KC.LGUI,     KC.LALT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LALT,     KC.LGUI,     xxxxx,
    #     xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,
    #     xxxxx,       xxxxx,       KC.ESC,      KC.MB_MMB,   KC.MB_LMB,   KC.MB_RMB,   xxxxx,       xxxxx,       KC.MB_RMB,   KC.MB_LMB,   KC.MB_MMB,   xxxxx,       xxxxx,       xxxxx,
    # ]
    # mapping["Nav"] = [
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    #     xxxxx,       KD.TD_NORELOAD, KD.TD_NODF2,    KD.TD_NODF1,    KD.TD_NODF0,    xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,
    #     xxxxx,       KC.LGUI,     KC.LALT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       KD.TD_CWCAPS,   KC.LEFT,     KC.DOWN,     KC.UP,       KC.RGHT,     xxxxx,
    #     xxxxx,       xxxxx,       KC.RALT,     KD.TD_NODF7,    KD.TD_NODF4,    xxxxx,       xxxxx,       xxxxx,       KC.INS,      KC.HOME,     KC.PGDN,     KC.PGUP,     KC.END,      xxxxx,
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.ENT,      KC.BSPC,     KC.DEL,      xxxxx,       xxxxx,       xxxxx,
    # ]
    # mapping["Mouse"] = [
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    #     xxxxx,       KD.TD_NORELOAD, KD.TD_NODF2,    KD.TD_NODF1,    KD.TD_NODF0,    xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,
    #     xxxxx,       KC.LGUI,     KC.LALT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.MS_LT,    KC.MS_DN,    KC.MS_UP,    KC.MS_RT,    xxxxx,
    #     xxxxx,       xxxxx,       KC.RALT,     KD.TD_NODF8,    KD.TD_NODF5,    xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.MW_DN,    KC.MW_UP,    xxxxx,       xxxxx,
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.MB_RMB,   KC.MB_LMB,   KC.MB_MMB,   xxxxx,       xxxxx,       xxxxx,
    # ]
    # mapping["Media"] = [
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    #     xxxxx,       KD.TD_NORELOAD, KD.TD_NODF2,    KD.TD_NODF1,    KD.TD_NODF0,    xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    #     xxxxx,       KC.LGUI,     KC.LALT,     KC.LCTL,     KC.LSFT,     xxxxx,       xxxxx,       xxxxx,       KC.PS_TOG,   KC.MPRV,     KC.VOLD,     KC.VOLU,     KC.MNXT,     xxxxx,
    #     xxxxx,       xxxxx,       KC.RALT,     KD.TD_NODF9,    KD.TD_NODF6,    xxxxx,       xxxxx,       xxxxx,       KC.HID,      xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.MSTP,     KC.MPLY,     KC.MUTE,     xxxxx,       xxxxx,       xxxxx,
    # ]
    # mapping["Num"] = [
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    #     xxxxx,       KC.LBRC,     KC.N7,       KC.N8,       KC.N9,       KC.RBRC,     xxxxx,       xxxxx,       xxxxx,       KD.TD_NODF0,    KD.TD_NODF1,    KD.TD_NODF2,    KD.TD_NORELOAD, xxxxx,
    #     xxxxx,       KC.SCLN,     KC.N4,       KC.N5,       KC.N6,       KC.EQL,      xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LALT,     KC.LGUI,     xxxxx,
    #     xxxxx,       KC.GRV,      KC.N1,       KC.N2,       KC.N3,       KC.BSLS,     xxxxx,       xxxxx,       xxxxx,       KD.TD_NODF7,    KD.TD_NODF4,    KC.RALT,     xxxxx,       xxxxx,
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       KC.DOT,      KC.N0,       KC.MINS,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    # ]
    # mapping["Sym"] = [
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    #     xxxxx,       KC.LCBR,     KC.AMPR,     KC.ASTR,     KC.LPRN,     KC.RCBR,     xxxxx,       xxxxx,       xxxxx,       KD.TD_NODF0,    KD.TD_NODF1,    KD.TD_NODF2,    KD.TD_NORELOAD, xxxxx,
    #     xxxxx,       KC.COLN,     KC.DLR,      KC.PERC,     KC.CIRC,     KC.PLUS,     xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LALT,     KC.LGUI,     xxxxx,
    #     xxxxx,       KC.TILD,     KC.EXLM,     KC.AT,       KC.HASH,     KC.PIPE,     xxxxx,       xxxxx,       xxxxx,       KD.TD_NODF8,    KD.TD_NODF5,    KC.RALT,     xxxxx,       xxxxx,
    #     xxxxx,       xxxxx,       xxxxx,       KC.LPRN,     KC.RPRN,     KC.UNDS,     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    # ]
    # mapping["Fun"] = [
    #     xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    #     xxxxx,       KC.F12,      KC.F7,       KC.F8,       KC.F9,       KC.PSCR,     xxxxx,       xxxxx,       xxxxx,       KD.TD_NODF0,    KD.TD_NODF1,    KD.TD_NODF2,    KD.TD_NORELOAD, xxxxx,
    #     xxxxx,       KC.F11,      KC.F4,       KC.F5,       KC.F6,       KC.SLCK,     xxxxx,       xxxxx,       xxxxx,       KC.LSFT,     KC.LCTL,     KC.LALT,     KC.LGUI,     xxxxx,
    #     xxxxx,       KC.F10,      KC.F1,       KC.F2,       KC.F3,       KC.PAUS,     xxxxx,       xxxxx,       xxxxx,       KD.TD_NODF9,    KD.TD_NODF6,    KC.RALT,     xxxxx,       xxxxx,
    #     xxxxx,       xxxxx,       xxxxx,       KC.APP,      KC.SPC,      KC.TAB,      xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,       xxxxx,
    # ]
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
