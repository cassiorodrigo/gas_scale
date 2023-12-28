from scale import Scale
from leds import LedStrip
import time


leds = LedStrip()


def main():
    
    scale = Scale()
    tara_q = input("Tare the scale [y/n]: ")
    if tara_q.upper() == 'Y':
        scale.tara()
    while True:
        if scale.is_ready():
#             print((scale.read()-scale.tara_value)/scale.cal_constant, end='\r')
            weight = scale.read_mean()
            leds.show(weight)
            print(scale.read_mean(), end='\r')
            
    
# while True:
#     if scale.is_ready():
#         cal = 1
#         ready = "No"
#         cont = False
#         leds_to_light = 0
#         while not cont:
#             ready = input("remove the weight and send a 't' to tare. Else, press enter: ")
#             if ready == 't':
#                 print("achei o t")
#                 tara_value = scale.read()
#                 print(f"{tara_value=}")
#                 time.sleep(2)
#             else:
#                 tara_value = 371933
#             calibrate_option = input("Calibrate the sacle [y/n]: ")
#             if calibrate_option.upper() == 'Y':
#                 cal = calibrate_scale(tara_weight=tara_value)
#             else:
#                 cal = -21.32897
#             cont = True
#         while True:
#             weight = (scale.read()) - tara_value
#             calibrated_weight = weight/cal
#             print(calibrated_weight, end='\r')
#             new_leds_to_light = show(calibrated_weight)
#             if new_leds_to_light != leds_to_light:
#                 leds_to_light = new_leds_to_light            
#                 
#                 clear()

try:
    main()
except KeyboardInterrupt:
    leds.clear()
except Exception:
    leds.clear()
