# 🐍 Austin's Python Projects

A collection of Python tools for Automation, IoT, Ham Radio, and System Administration.

Welcome to my coding playground. This repository hosts various scripts I've built to solve real-world problems, from monitoring air quality on a Raspberry Pi to debloating Android phones.

---

## 🔐 Cybersecurity & Network Tools (New!)

**Advanced networking scripts running on Fedora Linux (Headless Environment).**

### 🕷️ `spectre_scan.py` - Multi-Threaded Port Scanner
A reconnaissance tool built to analyze local networks for open ports and services.
* **Tech Stack:** Python `socket`, `threading` (100 concurrent threads), `queue`.
* **Features:** Scans range 1-1024 for "Well Known Ports," detects service names, and identifies firewall "stealth drops."
* **Use Case:** Network vulnerability assessment and identifying "invisible" IoT devices.

### 🖥️ `dashboard.py` - The Spectre Command Center
A Full-Stack Web Application that provides a GUI for the network scanner.
* **Tech Stack:** Python Flask (Backend), HTML/CSS (Frontend).
* **Architecture:** Demonstrates a **Client-Server model** where a Windows browser communicates with a Linux backend via SSH tunneling (Port 5000).
* **Features:** Dark Mode "Hacker" aesthetic, real-time scan initiation, and visual results table.

### 🏴‍☠️ `cyber_flag.py` - GUI Graphics over SSH
A graphical Python script demonstrating **X11 Forwarding** capabilities.
* **Tech Stack:** Python `turtle`, `tkinter`.
* **Concept:** Uses the Turtle graphics engine to draw a "Cyber-Jolly Roger" flag.
* **Significance:** Proves the capability to run graphical Linux applications remotely on a Windows host via an encrypted SSH tunnel.

---

## ☁️ IoT & Hardware Projects

**Hardware-integrated scripts for the DeVry "Intro to IoT" curriculum.**

### 🌡️ `bme680_reader.py` - All-in-One Air Quality Meter
A sensor interface designed for the **Raspberry Pi** using the **BME680** sensor to track environmental data.
* **Cross-Platform Simulation Mode:** Includes a smart `try/except` block that detects if the script is running on a Windows PC (without GPIO) or a Raspberry Pi. It automatically switches to simulated data on Windows for testing logic without hardware.
* **Data Points:** Reads real-time Temperature (°F), Humidity (%), Barometric Pressure (hPa), and Gas Resistance (VOCs).
* **Logic:** Calculates air quality status (Excellent/Good/Poor) based on raw gas resistance readings.
* **Hardware:** Raspberry Pi 4, Adafruit BME680 Sensor.

---

## 📱 Android Automation Tools

**Powered by ADB (Android Debug Bridge) & Python**

### 🛠️ `debloat.py` - The Bloatware Killer
A surgical tool designed to speed up budget Android devices (specifically the **Cloud Mobile AS65U**) by removing carrier bloatware and resource-heavy system apps.
* **Features:** Automatically detects connected phone via ADB and removes 40+ pre-identified bloatware packages.
* **Safe Mode:** Skips essential system apps (Launcher, Keyboard) to prevent bricking.

### 📡 `telemetry.py` - Live Signal Monitor
A real-time dashboard that turns an Android phone into a Wi-Fi and Battery telemetry sensor.
* **Features:** Live stream of Wi-Fi Signal Strength (RSSI in dBm), battery voltage, and temperature monitoring.
* **Tech:** Uses Regex parsing to handle non-standard log outputs from budget phones.

---

## 📻 Ham Radio Utilities

**Tools for Amateur Radio operators (Callsign: [Your Callsign Here])**

* **`antenna_calc.py`:** Calculates the optimal length for dipole antennas based on frequency.
* **`radio_horizon.py`:** Determines the visual and radio horizon distance based on antenna height.
* **`oop_radio_horizon.py`:** An Object-Oriented version of the horizon calculator.

---

## 💻 Core Python Concepts

**Scripts demonstrating fundamental programming principles.**

* **`pingsweep.py`:** A network scanner to detect active devices on a local network.
* **`oop_encapsulation.py`:** Demonstrates secure data handling using Getters/Setters.
* **`oop_inheritance.py`:** Examples of class inheritance and hierarchy.
* **`oop_polymorphism.py`:** Examples of flexible function usage across different classes.

---

## 🖥️ Development Environment

My current tech stack and development workspace include:
* **OS:** Windows 11 (Host), **Fedora Workstation 43** (Headless Server), and Kali Linux (VM).
* **Hardware:** HP Victus (i5-12450H, RTX 3050), Raspberry Pi.
* **Tools:** VS Code (Remote-SSH), ADB, Baofeng/Tidradio (Ham operations).

## ⚙️ Setup & Requirements

To run the Android, IoT, and Web tools, you will need:

```bash
# For Android Tools
pip install pure-python-adb

# For IoT/Air Quality Tools (Requires CircuitPython support)
pip install adafruit-circuitpython-bme680

# For Web Dashboard & Graphics
pip install flask
sudo dnf install python3-tkinter  # (On Fedora/Linux)
