from kmk.keys import KC

`5432`
def get_definitions(tap_time):
    _____ = KC.TRNS
    xxxxx = KC.NO
    ooooo = KC.NO  # THIS one is that there is no phsycical key

    class KD:
        LT_3SLSH = KC.LT(3, KC.SLSH, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
        LT_3Z = KC.LT(3, KC.Z, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
        LT_4SPC = KC.LT(4, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
        LT_5TAB = KC.LT(5, KC.TAB, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
        LT_6ESC = KC.LT(6, KC.ESC, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
        LT_7BSPC = KC.LT(7, KC.BSPC, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
        LT_8ENT = KC.LT(8, KC.ENT, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
        LT_9DEL = KC.LT(9, KC.DEL, prefer_hold=True, tap_interrupted=False, tap_time=tap_time)
        HT_ALGUI = KC.HT(
            KC.A,
            KC.LGUI,
            prefer_hold=False,
            tap_interrupted=True,
            tap_time=tap_time,
        )
        HT_SLCTL = KC.HT(
            KC.S,
            KC.LCTL,
            prefer_hold=False,
            tap_interrupted=True,
            tap_time=tap_time,
        )
        HT_DOTRALT = KC.HT(
            KC.DOT,
            KC.RALT,
            prefer_hold=False,
            tap_interrupted=True,
            tap_time=tap_time,
        )
        HT_TLSFT = KC.HT(
            KC.T,
            KC.LSFT,
            prefer_hold=False,
            tap_interrupted=True,
            tap_time=tap_time,
        )
        HT_NLSFT = KC.HT(
            KC.N,
            KC.LSFT,
            prefer_hold=False,
            tap_interrupted=True,
            tap_time=tap_time,
        )
        HT_ELCTL = KC.HT(
            KC.E,
            KC.LCTL,
            prefer_hold=False,
            tap_interrupted=True,
            tap_time=tap_time,
        )
        HT_ILALT = KC.HT(
            KC.I,
            KC.LALT,
            prefer_hold=False,
            tap_interrupted=True,
            tap_time=tap_time,
        )
        HT_OLGUI = KC.HT(
            KC.O,
            KC.LGUI,
            prefer_hold=False,
            tap_interrupted=True,
            tap_time=tap_time,
        )
        HT_SLALT = KC.HT(
            KC.R,
            KC.LALT,
            prefer_hold=False,
            tap_interrupted=True,
            tap_time=tap_time,
        )
        HT_XRALT = KC.HT(
            KC.X,
            KC.RALT,
            prefer_hold=False,
            tap_interrupted=True,
            tap_time=tap_time,
        )
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

    return KD
