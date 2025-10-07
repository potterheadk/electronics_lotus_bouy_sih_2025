# electronics_lotus_bouy_sih_2025
sih-2025 project electronics




# 💧 Smart Water Quality Monitoring System

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Project-red?logo=raspberrypi)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

> 🌊 Measure real-time water quality using Turbidity, pH, and Temperature sensors connected to a Raspberry Pi with ADS1115 ADC.

---

## 📘 Project Overview

This system monitors **key water parameters** in real-time:  

- 🌡 **Temperature (°C)** — DS18B20 sensor  
- ⚗️ **pH** — 0–14 analog sensor  
- 💧 **Turbidity (NTU)** — analog turbidity sensor  

The system reads sensor values via **ADS1115 ADC** and **GPIO**, converts them to real-world units, and prints/logs them.  

---

## 🧰 Hardware Components

| Component          | Description                  | Qty |
|------------------|-----------------------------|-----|
| Raspberry Pi 3B+  | Main controller             | 1   |
| ADS1115           | 16-bit ADC (I²C)            | 1   |
| Turbidity Sensor  | Analog clarity sensor       | 1   |
| pH Sensor         | Analog pH 0–14 sensor       | 1   |
| DS18B20           | Digital temperature sensor  | 1   |
| 4.7 kΩ Resistor   | Pull-up for DS18B20         | 1   |
| Breadboard & Wires| Jumper connections          | —   |

---

## 🔌 Connection Guide (ASCII Diagram)

```

```
  +------------------+
  | Raspberry Pi 3B+ |
  |                  |
```

3.3V | 1 -------------+  VCC DS18B20
5V   | 2 -------------+  VCC pH/Turbidity Sensor
SDA1 | 3 -------------+  SDA ADS1115
SCL1 | 5 -------------+  SCL ADS1115
GND  | 6 -------------+  GND (all sensors)
GPIO4| 7 -------------+  DQ DS18B20 (with 4.7kΩ pull-up to 3.3V)
+------------------+

ADS1115 Channels:
A0  <- Turbidity AO
A1  <- pH AO

````
Perfect 🌊 — since your setup includes **turbidity**, **pH**, and **temperature** sensors connected to a **Raspberry Pi**, here’s a complete and professional **README.md** you can include in your GitHub repo or documentation folder.

It’s written to be clear for both beginners and developers who want to replicate or extend your water-quality monitoring system.

---

# 💧 Smart Water Quality Monitoring using Raspberry Pi

### 🧠 Sensors: Turbidity | pH | Temperature (DS18B20)

### 🧩 ADC: ADS1115 (I²C Interface)

### 🐍 Language: Python 3

### ⚙️ Platform: Raspberry Pi 3B/3B+/4

---

## 📜 Overview

This project measures **real-time water quality parameters** using affordable sensors and a Raspberry Pi.
It captures:

* **Turbidity (NTU)** – water clarity
* **pH level** – acidity/basicity
* **Temperature (°C)** – water temperature

All readings are displayed live in the terminal, and can easily be extended to a dashboard or cloud platform (like ThingsBoard, Firebase, or MQTT broker).

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
| Jumper Wires          | Male–Female and Male–Male   | —        |
| Breadboard            | For easy wiring             | 1        |

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

| Sensor           | Signal Pin | ADS1115 Channel | Power    |
| ---------------- | ---------- | --------------- | -------- |
| Turbidity Sensor | AO         | A0              | VCC = 5V |
| pH Sensor        | AO         | A1              | VCC = 5V |

---

### **DS18B20 → Raspberry Pi**

| DS18B20 Pin | Connects To    | Notes                                          |
| ----------- | -------------- | ---------------------------------------------- |
| VCC         | 3.3V           | —                                              |
| GND         | GND            | —                                              |
| DATA        | GPIO 4 (Pin 7) | 4.7kΩ pull-up resistor between **DATA ↔ 3.3V** |

---


**Notes:**  
- DS18B20: Yellow DATA line → GPIO 4, with 4.7kΩ pull-up to 3.3V.  
- Turbidity & pH sensors powered by 5V, but ADC reads at 3.3V logic.  
- ADS1115 communicates via I²C (SDA → GPIO2, SCL → GPIO3).  

---

## ⚙️ Software Setup

### 1️⃣ Enable Interfaces
```bash
sudo raspi-config
````

Enable:

* I²C
* 1-Wire

Then reboot:

```bash
sudo reboot
```

### 2️⃣ Install Dependencies

```bash
sudo apt update
sudo apt install python3-pip -y
pip install adafruit-circuitpython-ads1x15 adafruit-circuitpython-ds18x20 adafruit-circuitpython-busdevice
```

---

## 🧮 Sensor Formulas

### 🌡 Temperature (DS18B20)

* Sensor directly provides temperature in °C.
* Code reads `/sys/bus/w1/devices/28-xxxx/w1_slave` and extracts value.

### ⚗️ pH Sensor

```text
pH = 7 + ((V_ref - V_measured) * 3.5)
```

* `V_ref ≈ 2.5V` for pH 7 (neutral)
* Voltage measured from ADC

### 💧 Turbidity Sensor

```text
Turbidity_NTU = max(0, NTU_max - (Voltage_measured * scale))
```

* Adjust `NTU_max` and `scale` based on calibration with clear and muddy water.

---

## 🧩 Python Scripts

* **`temp_sensor.py`** — Reads DS18B20
* **`ph_sensor.py`** — Reads pH from ADC
* **`turbidity_sensor.py`** — Reads turbidity from ADC
* **`main.py`** — Unified script for all three sensors

---

## 🧪 Calibration Tips

| Sensor          | Calibration                                                             |
| --------------- | ----------------------------------------------------------------------- |
| **pH**          | Use pH buffer solutions (4, 7, 10) to adjust slope/offset in formula.   |
| **Turbidity**   | Calibrate with distilled water (0 NTU) and muddy water for maximum NTU. |
| **Temperature** | Compare against a calibrated thermometer.                               |

---

## 💻 Accessing Raspberry Pi via SSH

1. Find Raspberry Pi IP:

```bash
hostname -I
```

2. From your PC / Laptop:

```bash
ssh pi@<RPI_IP_ADDRESS>
```

* Default password: `raspberry`
* Enable SSH via `sudo raspi-config` → Interface Options → SSH

3. Run scripts remotely:

```bash
cd ~/sih_lotus_buoy
source myenv/bin/activate
python3 main.py
```

---

## 🔧 How to Modify

* **Add more sensors:** Connect additional analog sensors to ADS1115 channels (A2, A3).
* **Change formulas:** Adjust `voltage_to_ph` or `voltage_to_ntu` based on calibration data.
* **Data logging:** Add CSV / database writing code in `main.py`.
* **Cloud integration:** Use MQTT or HTTP POST to send sensor data to a server.

---

## 📈 Future Enhancements

* Live web dashboard (React / Angular / Flask)
* Real-time alerts with LEDs, buzzer, or SMS
* TinyML model for automatic water-quality classification
* Integration with IoT cloud platforms

---

## 🧾 License

MIT License © 2025
Developed by *Your Team Name*

---

### 💡 “Clean water is everyone’s right — monitor, act, protect.” 🌍
