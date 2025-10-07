import time
import board, busio, glob, os
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# --- ADC Setup ---
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
turbidity_chan = AnalogIn(ads, ADS.P0)
ph_chan = AnalogIn(ads, ADS.P1)

# --- DS18B20 Setup ---
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28-*')[0]
device_file = device_folder + '/w1_slave'

def read_temp():
    with open(device_file, 'r') as f:
        lines = f.readlines()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        with open(device_file, 'r') as f:
            lines = f.readlines()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        return float(lines[1][equals_pos + 2:]) / 1000.0

def voltage_to_ntu(v): return max(0, 3000 - (v * 1800))
def voltage_to_ph(v): return round(7 + ((2.5 - v) * 3.5), 2)

print("🌊 Real-Time Water Quality Monitor 🌊\nPress Ctrl+C to stop.\n")

try:
    while True:
        temp = read_temp()
        turbidity = voltage_to_ntu(turbidity_chan.voltage)
        ph = voltage_to_ph(ph_chan.voltage)
        print(f"Temp: {temp:.2f}°C | Turbidity: {turbidity:.1f} NTU | pH: {ph}")
        time.sleep(1)
except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped.")
