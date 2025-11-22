# python-intro
# 🐍 Austin's Python Projects
*> A collection of Python tools for Automation, Ham Radio, and System Administration.*

Welcome to my coding playground. This repository hosts various scripts I've built to solve real-world problems, from calculating radio antenna resonance to debloating Android phones.

---

## 📱 Android Automation Tools (New!)
*Powered by ADB (Android Debug Bridge) & Python*

### 🛠️ `debloat.py` - The Bloatware Killer
A surgical tool designed to speed up budget Android devices (specifically the **Cloud Mobile AS65U**) by removing carrier bloatware and resource-heavy system apps.
- **Features:** - Automatically detects connected phone via ADB.
  - Removes 40+ pre-identified bloatware packages (Carrier apps, Facebook services, Unisoc loggers).
  - Safe Mode: Skips essential system apps (Launcher, Keyboard) to prevent bricking.
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

## ⚙️ Setup & Requirements

To run the Android tools, you need the `pure-python-adb` library:

```bash
pip install pure-python-adb