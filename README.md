# python-intro
# 🐍 Austin's Python Projects
> *A collection of Python tools for Automation, IoT, Ham Radio, and System Administration.*

Welcome to my coding playground. This repository hosts various scripts I've built to solve real-world problems, from monitoring air quality on a Raspberry Pi to debloating Android phones.

---

## ☁️ IoT & Hardware Projects (New!)
*Hardware-integrated scripts for the DeVry "Intro to IoT" curriculum.*

### 🌡️ `bme680_reader.py` - All-in-One Air Quality Meter
A sensor interface designed for the **Raspberry Pi** using the **BME680** sensor to track environmental data.
- **Features:**
  - **Cross-Platform Simulation Mode:** Includes a smart `try/except` block that detects if the script is running on a Windows PC (without GPIO) or a Raspberry Pi. It automatically switches to simulated data on Windows for testing logic without hardware.
  - **Data Points:** Reads real-time Temperature (°F), Humidity (%), Barometric Pressure (hPa), and Gas Resistance (VOCs).
  - **Logic:** Calculates air quality status (Excellent/Good/Poor) based on raw gas resistance readings.
  - **Hardware:** Raspberry Pi 4, Adafruit BME680 Sensor.

---

## 📱 Android Automation Tools
*Powered by ADB (Android Debug Bridge) & Python*

### 🛠️ `debloat.py` - The Bloatware Killer
A surgical tool designed to speed up budget Android devices (specifically the **Cloud Mobile AS65U**) by removing carrier bloatware and resource-heavy system apps.
- **Features:**
  - Automatically detects connected phone via ADB.
  - Removes 40+ pre-identified bloatware packages (Carrier apps, Facebook services, Unisoc loggers).
  - **Safe Mode:** Skips essential system apps (Launcher, Keyboard) to prevent bricking.
  - **Usage:** `python debloat.py`

### 📡 `telemetry.py` - Live Signal Monitor
A real-time dashboard that turns an Android phone into a Wi-Fi and Battery telemetry sensor.
- **Features:**
  - Live stream of Wi-Fi Signal Strength (RSSI in dBm).
  - Battery voltage and temperature monitoring.
  - Regex parsing to handle non-standard log outputs from budget phones.
  - **Usage:** `python telemetry.py` (Great for site surveys/war driving).

---

## 📻 Ham Radio Utilities
*Tools for Amateur Radio operators (Callsign: [Your Callsign Here])*

- **`antenna_calc.py`**: Calculates the optimal length for dipole antennas based on frequency.
- **`radio_horizon.py`**: Determines the visual and radio horizon distance based on antenna height.
- **`oop_radio_horizon.py`**: An Object-Oriented version of the horizon calculator (demonstrating Class structures).

---

## 💻 Core Python Concepts
*Scripts demonstrating fundamental programming principles.*

- **`pingsweep.py`**: A network scanner to detect active devices on a local network.
- **`oop_encapsulation.py`**: Demonstrates secure data handling using Getters/Setters.
- **`oop_inheritance.py`**: Examples of class inheritance and hierarchy.
- **`oop_polymorphism.py`**: Examples of flexible function usage across different classes.

---

## 🖥️ Development Environment
My current tech stack and development workspace include:
- **OS:** Windows 11 (Host), **Fedora Workstation** (VM), and **Kali Linux** (VM) for penetration testing and security labs.
- **Hardware:** HP Victus (i5-12450H, RTX 3050), Raspberry Pi.
- **Tools:** VS Code, ADB, Baofeng/Tidradio (Ham operations).

---

## ⚙️ Setup & Requirements

To run the Android and IoT tools, you will need the following libraries:

```bash
# For Android Tools
pip install pure-python-adb

# For IoT/Air Quality Tools (Requires CircuitPython support)
pip install adafruit-circuitpython-bme680