import time
import sys
import re  # <--- New tool for finding patterns
from ppadb.client import Client as AdbClient

# Connect to ADB
client = AdbClient(host="127.0.0.1", port=5037)
try:
    devices = client.devices()
except Exception as e:
    print("❌ ADB Server not running. Run 'adb start-server' in terminal.")
    sys.exit()

if not devices:
    print("❌ No phone found. Make sure it's plugged in via USB.")
    sys.exit()

device = devices[0]
model = device.shell("getprop ro.product.model").strip()

print(f"📡 Connected to {model} (AS65U). Starting Telemetry...")
print("-" * 60)
print(f"{'TIME':<10} | {'BATTERY':<10} | {'SIGNAL (dBm)':<15} | {'STATUS'}")
print("-" * 60)

try:
    while True:
        # 1. Get Battery Level
        bat_raw = device.shell("dumpsys battery")
        level = "N/A"
        for line in bat_raw.split('\n'):
            if "level" in line:
                level = line.split(':')[1].strip() + "%"
        
        # 2. Get Wi-Fi Signal (The Fix for your specific phone)
        # We grab the specific line 'mWifiInfo' which we saw in your screenshot
        wifi_raw = device.shell("dumpsys wifi | grep mWifiInfo")
        
        rssi = "No Signal"
        # Regex pattern: Look for 'RSSI:', optional space (\s*), then a number (-?\d+)
        match = re.search(r'RSSI:\s*(-?\d+)', wifi_raw)
        
        if match:
            rssi = match.group(1) + " dBm"

        # 3. Print Data
        current_time = time.strftime("%H:%M:%S")
        print(f"{current_time:<10} | {level:<10} | {rssi:<15} | Monitoring...")
        
        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Telemetry stopped.")