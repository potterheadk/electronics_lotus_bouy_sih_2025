import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)

def voltage_to_ntu(voltage):
    # Adjust calibration curve for your sensor
    return max(0, 3000 - (voltage * 1800))

print("Reading turbidity in NTU... Press Ctrl+C to stop.")
while True:
    voltage = chan.voltage
    ntu = voltage_to_ntu(voltage)
    print(f"Voltage: {voltage:.3f} V, Turbidity: {ntu:.2f} NTU")
    time.sleep(1)
