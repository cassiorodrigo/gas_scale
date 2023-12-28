from hx711 import HX711
from leds import show, clear
import time


scale = HX711(
    d_out=25,
    pd_sck=26
    )

def calibrate_scale(cal_weight: float=535.0, tara_weight: int=372318):
    print(f"Set the weight on the scale now.")
    custom_weight = input("Use custom weight? If want to use 535, leave it empty. Otherwise, type it just the numbers: ")
    weight = scale.read()-tara_weight
    if custom_weight:
        print(f"Using {custom_weight=} as calibration value.")
        cal_weight = float(custom_weight)
    else:
        print(f"Using {cal_weight=} as calibration value.")
        
    calibration_factor = weight/cal_weight
    
    print(f"Calibration factor: {calibration_factor=}")
    return calibration_factor

while True:
    if scale.is_ready():
        cal = 1
        ready = "No"
        cont = False
        leds_to_light = 0
        while not cont:
            ready = input("remove the weight and send a 't' to tare. Else, press enter: ")
            if ready == 't':
                print("achei o t")
                tara_value = scale.read()
                print(f"{tara_value=}")
                time.sleep(2)
            else:
                tara_value = 371933
            calibrate_option = input("Calibrate the sacle [y/n]: ")
            if calibrate_option.upper() == 'Y':
                cal = calibrate_scale(tara_weight=tara_value)
            else:
                cal = -21.32897
            cont = True
        while True:
            weight = (scale.read()) - tara_value
            calibrated_weight = weight/cal
            print(calibrated_weight, end='\r')
            new_leds_to_light = show(calibrated_weight)
            if new_leds_to_light != leds_to_light:
                leds_to_light = new_leds_to_light            
                
                clear()
