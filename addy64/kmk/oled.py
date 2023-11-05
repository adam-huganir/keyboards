import busio
import gc

import adafruit_displayio_ssd1306
import displayio
import terminalio
from adafruit_display_text import label

from kmk.extensions import Extension
from kmk.extensions.peg_oled_display import *


class CustomOled(Oled):
    def __init__(
        self,
        views,
        i2c,
        toDisplay=OledDisplayMode.TXT,
        oWidth=128,
        oHeight=32,
        flip: bool = False,
        font=None,
    ):
        displayio.release_displays()
        self.rotation = 180 if flip else 0
        self._views = views
        self._toDisplay = toDisplay
        self._width = oWidth
        self._height = oHeight
        self._prevLayers = 0
        self._i2c = i2c
        self._font = font or terminalio.FONT
        alpha = list(range(ord("A"), ord("Z")))
        self._font_height = max([self._font.get_glyph(i).height for i in alpha])
        self._font_weight_avg = sum([self._font.get_glyph(i).width for i in alpha]) / len(alpha)
        gc.collect()

    def updateOLED(self, sandbox):
        layer = sandbox.active_layers[0]
        self.run_layers(layer)

    def run_layers(self, layer):
        splash = displayio.Group()
        for v in self._views:
            splash.append(v[0](self, layer))
        self._display.show(splash)
        gc.collect()

    def returnCurrectRenderText(self, layer, singleView):
        print(singleView)
        return singleView[1][layer]

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, keyboard):
        displayio.release_displays()
        i2c = self._i2c
        self._display = adafruit_displayio_ssd1306.SSD1306(
            displayio.I2CDisplay(i2c, device_address=0x3C),
            width=self._width,
            height=self._height,
            rotation=self.rotation,
        )

        self.run_layers(0)
        return

    def before_matrix_scan(self, sandbox):
        if sandbox.active_layers[0] != self._prevLayers:
            self._prevLayers = sandbox.active_layers[0]
            self.updateOLED(sandbox)
        # if sandbox.matrix_update:
        #     self.updateOLED_key_change(sandbox)
        return

    # def updateOLED_key_change(self, sandbox):
    #         layer = sandbox.active_layers[0]
    #         event: KeyEvent = sandbox.matrix_update
    #         splash = displayio.Group()
    #         for v in self._views:
    #             splash.append(v(self, layer))
    #         self._display.show(splash)
    #         gc.collect()

    def after_matrix_scan(self, sandbox):
        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return
