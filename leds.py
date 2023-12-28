from neopixel import NeoPixel
from machine import Pin
from math import ceil


class Weight:
    MAX_WEIGHT = 1.0
    
class LedStrip:
    
    def __init__(self):
        self.DATA_PIN = 27
        self.LED_LENGTH = 19
        self.MAX_BRIGHTNESS = 5
        self.np = NeoPixel(Pin(self.DATA_PIN), self.LED_LENGTH+1)
        self.np[19] = (10, 10, 10)
        self.np.write()
        self.last_leds = None


    def clear(self):
        for led in range(self.LED_LENGTH+1):
            self.np[led] = (0, 0, 0)
            self.np.write()

    def calc_led(self, weight):
        use_max_weight = Weight.MAX_WEIGHT
        if weight > use_max_weight:
            Weight.MAX_WEIGHT = weight
        porcentagem = (weight/use_max_weight)*100
        leds = ceil(((weight*100)/use_max_weight*self.LED_LENGTH)/100)
        if leds > self.LED_LENGTH:
            leds = self.LED_LENGTH
        elif leds < 0:
            leds = 0
        if leds != self.last_leds:
            self.last_leds = leds
            self.clear()
        return leds, porcentagem

    def cor(self, porcentagem):
        if int(porcentagem >= 75):
            return (0, self.MAX_BRIGHTNESS, 0)
        elif int(porcentagem >= 45) and int(porcentagem <75):
            return (self.MAX_BRIGHTNESS, 3, 0)
        else:
            return (self.MAX_BRIGHTNESS, 0, 0)
        
        
    def show(self, weight: float=535):
        
        self.calc_led(weight=weight)
        leds, porcentagem = self.calc_led(weight=weight)
        color = self.cor(porcentagem)
        for led in range(leds):
            self.np[led] = color
            self.np.write()
        return leds
