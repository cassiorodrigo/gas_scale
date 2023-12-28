from neopixel import NeoPixel
from machine import Pin
from math import ceil


DATA_PIN = 27
LED_LENGTH = 19
MAX_BRIGHTNESS = 5
np = NeoPixel(Pin(DATA_PIN), LED_LENGTH+1)
np[19] = (10, 10, 10)
np.write()

class Weight:
    MAX_WEIGHT = 1.0


def clear():
    for led in range(LED_LENGTH+1):
        np[led] = (0, 0, 0)
        np.write()


def calc_led(weight):
    use_max_weight = Weight.MAX_WEIGHT
    if weight > use_max_weight:
        Weight.MAX_WEIGHT = weight
    porcentagem = (weight/use_max_weight)*100
    leds = ceil(((weight*100)/use_max_weight*LED_LENGTH)/100)
    if leds > LED_LENGTH:
        leds = LED_LENGTH
    elif leds < 0:
        leds = 0
    return leds, porcentagem

def cor(porcentagem):
    if int(porcentagem >= 75):
        return (0, MAX_BRIGHTNESS, 0)
    elif int(porcentagem >= 45) and int(porcentagem <75):
        return (MAX_BRIGHTNESS, 3, 0)
    else:
        return (MAX_BRIGHTNESS, 0, 0)
    
    
def show(weight: float=535):
    
    calc_led(weight=weight)
    leds, porcentagem = calc_led(weight=weight)
    color = cor(porcentagem)
    for led in range(leds):
        np[led] = color
        np.write()
    return leds

