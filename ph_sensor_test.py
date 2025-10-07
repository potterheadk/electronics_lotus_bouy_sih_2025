import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P1)

def voltage_to_ph(voltage):
    # Calibrate using known solutions
    return round(7 + ((2.5 - voltage) * 3.5), 2)

while True:
    voltage = chan.voltage
    ph = voltage_to_ph(voltage)
    print(f"Voltage: {voltage:.3f} V, pH: {ph}")
    time.sleep(1)
