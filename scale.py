from hx711 import HX711
from time import sleep_us
from math import ceil


class Scale(HX711):
    """Custom Scale class to implement new methods like: calibration and tara."""
    def __init__(self):
        self.scale = super().__init__(
            d_out=25,
            pd_sck=26
            )
        self.tara_value = 371933  # pre-stabilished tara value.
        self.cal_constant = -21.32897  # pre-stabilished calibration constant
        self.full_vessel_weight = 535.0  # weight used for calibration. This is for initializing with the calibrated weight.

    def calibrate_scale(self, cal_weight: float=535.0):
        print(f"Set the weight on the scale now.")
        custom_weight = input("Use custom weight? If want to use 535, leave it empty. Otherwise, type it just the numbers: ")
        weight = scale.read()-self.tara_value
        if custom_weight:
            print(f"Using {custom_weight=} as calibration value.")
            cal_weight = float(custom_weight)
        else:
            print(f"Using {cal_weight=} as calibration value.")
            
        self.cal_constant = weight/cal_weight
        
        print(f"Calibration factor: {calibration_factor=}")
        
    def tara(self):
        _res = input("Remove any weight from the scale and hit enter: ")
        self.tara_value = self.read_mean(read_times=20, raw=True)
        print(f"New tara falue: {self.tara_value}")
        
    def reset_full_vessel_weight(self):
        self.full_vessel_weight = self.read_mean(10)
        
        
    def read_mean(self, read_times: int=10, raw: bool=False):
        reads = []
        for _ in range(reads_times):
            reads.append(self.read())
            sleep_us(10)
        if max(reads)/min(reads) > 0.1:  # 10% error allowed
            print(f'More than 10% error on {read_times} reads. \nRestarting the read_mean method.')
            self.read_mean(read_times)
            
        mean = ceil(sum(reads)/read_times)
        if raw:
            return mean
        else:
            return (mean-self.tara_value)/self.cal_constant
    
    
            
