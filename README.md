
# 💧 Smart Water Quality Monitoring using Raspberry Pi

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Project-red?logo=raspberrypi)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![ADS1115](https://img.shields.io/badge/ADC-ADS1115-yellow)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

> 🌊 Measure real-time water quality using **Turbidity**, **pH**, and **Temperature** sensors connected to a **Raspberry Pi** with an **ADS1115 ADC** module.

---

## 📘 Project Overview

This system monitors **key water parameters** in real time:

- 🌡 **Temperature (°C)** — DS18B20 sensor  
- ⚗️ **pH** — 0–14 analog sensor  
- 💧 **Turbidity (NTU)** — analog turbidity sensor  

All sensors are read through the **ADS1115 (16-bit ADC)** and **GPIO**, converted into real-world units, and displayed or logged.  
The setup can be extended to cloud platforms (MQTT, Firebase, ThingsBoard) or dashboards for live monitoring.

---

## 🧰 Hardware Components

| Component             | Description                 | Quantity |
| --------------------- | --------------------------- | -------- |
| Raspberry Pi 3B/3B+/4 | Main controller             | 1        |
| ADS1115               | 16-bit ADC module (I²C)     | 1        |
| Turbidity Sensor      | Analog water clarity sensor | 1        |
| pH Sensor             | Analog pH 0–14 sensor       | 1        |
| DS18B20               | Digital temperature sensor  | 1        |
| 4.7kΩ Resistor        | Pull-up for DS18B20         | 1        |
| Jumper Wires          | Male–Female / Male–Male     | —        |
| Breadboard            | For easy wiring             | 1        |

---

## 🔌 Connection Guide

```text
  +------------------+
  | Raspberry Pi 3B+ |
  |                  |
  | 3.3V | 1 -------------+  VCC DS18B20
  | 5V   | 2 -------------+  VCC pH/Turbidity Sensor
  | SDA1 | 3 -------------+  SDA ADS1115
  | SCL1 | 5 -------------+  SCL ADS1115
  | GND  | 6 -------------+  GND (all sensors)
  | GPIO4| 7 -------------+  DQ DS18B20 (with 4.7kΩ pull-up to 3.3V)
  +------------------+

ADS1115 Channels:
A0  ← Turbidity AO  
A1  ← pH AO
````

---

## ⚙️ Pin Connections

### **ADS1115 → Raspberry Pi (I²C)**

| ADS1115 Pin | Raspberry Pi Pin | Function  |
| ----------- | ---------------- | --------- |
| VCC         | 3.3V             | Power     |
| GND         | GND              | Ground    |
| SDA         | GPIO 2 (Pin 3)   | I²C Data  |
| SCL         | GPIO 3 (Pin 5)   | I²C Clock |

---

### **Sensors → ADS1115**

| Sensor           | Signal Pin | ADS1115 Channel | Power |
| ---------------- | ---------- | --------------- | ----- |
| Turbidity Sensor | AO         | A0              | 5V    |
| pH Sensor        | AO         | A1              | 5V    |

---

### **DS18B20 → Raspberry Pi**

| DS18B20 Pin | Connects To    | Notes                                          |
| ----------- | -------------- | ---------------------------------------------- |
| VCC         | 3.3V           | —                                              |
| GND         | GND            | —                                              |
| DATA        | GPIO 4 (Pin 7) | 4.7kΩ pull-up resistor between **DATA ↔ 3.3V** |

---

## 📁 Project Structure

```text
electronics_lotus_buoy_sih_2025/
├── main.py
├── temp_sensor.py
├── ph_sensor.py
├── turbidity_sensor.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Software Setup

### 1️⃣ Enable Interfaces

```bash
sudo raspi-config
```

Enable:

* I²C
* 1-Wire

Then reboot:

```bash
sudo reboot
```

---

### 2️⃣ Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip -y
pip install adafruit-circuitpython-ads1x15 adafruit-circuitpython-ds18x20 adafruit-circuitpython-busdevice
```

---

## 🧮 Sensor Formulas

### 🌡 Temperature (DS18B20)

* Reads temperature directly in °C.
* Code reads `/sys/bus/w1/devices/28-xxxx/w1_slave`.

---

### ⚗️ pH Sensor

```python
pH = 7 + ((V_ref - V_measured) * 3.5)
```

* `V_ref ≈ 2.5V` for neutral pH 7
* Calibrate using buffer solutions for better accuracy

---

### 💧 Turbidity Sensor

```python
Turbidity_NTU = max(0, NTU_max - (Voltage_measured * scale))
```

* Adjust `NTU_max` and `scale` based on calibration data.
* Clear water ≈ 0 NTU, muddy water → higher NTU.

---

## 🧩 Python Scripts

| Script                | Function                                          |
| --------------------- | ------------------------------------------------- |
| `temp_sensor.py`      | Reads temperature from DS18B20                    |
| `ph_sensor.py`        | Reads and converts pH from ADC                    |
| `turbidity_sensor.py` | Reads turbidity voltage and converts to NTU       |
| `main.py`             | Integrates all sensors for unified output/logging |

---

## 🧪 Calibration Tips

| Sensor          | Calibration Method                                            |
| --------------- | ------------------------------------------------------------- |
| **pH**          | Use pH buffer solutions (4, 7, 10) to adjust slope and offset |
| **Turbidity**   | Calibrate with distilled (0 NTU) and muddy water              |
| **Temperature** | Compare against a calibrated thermometer                      |

---

## 💻 Accessing Raspberry Pi via SSH

1️⃣ Find your Raspberry Pi IP:

```bash
hostname -I
```

2️⃣ Connect from your PC:

```bash
ssh pi@<RPI_IP_ADDRESS>
```

*Default password*: `raspberry`

3️⃣ Run the project:

```bash
cd ~/electronics_lotus_buoy_sih_2025
python3 main.py
```

---

## 🔧 How to Modify

* **Add new sensors:** Use remaining ADS1115 channels (A2, A3).
* **Edit formulas:** Adjust calibration constants for your environment.
* **Data logging:** Write data to `.csv` or PostgreSQL database.
* **Cloud sync:** Send sensor data to IoT platforms via MQTT/HTTP.

---

## 📈 Future Enhancements

* 🌐 Live dashboard (Flask / React)
* 🚨 Real-time alerts (LED, buzzer, or SMS)
* 🤖 TinyML-based water-quality classification
* ☁️ IoT cloud integration (ThingsBoard, Firebase, AWS IoT)

---

## 🧾 License

**MIT License © 2025**
Developed by *Electronics Lotus Buoy — SIH 2025 Team*

setup seamless on any Raspberry Pi.
```
