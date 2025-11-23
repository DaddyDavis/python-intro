# --------------------------------------------------------------------------------------
# FILE: bme680_reader.py
# PROJECT: All-in-One Air Quality Meter for Intro to IoT
# DESCRIPTION: Reads temperature, humidity, pressure, and gas (VOC) data from a BME680 sensor.
#              This code simulates the readings if run on Windows, but is ready to run on a Pi.
# --------------------------------------------------------------------------------------

# We use the built-in 'time' library to pause the script between readings.
import time

# --- SENSOR LIBRARIES (installed in your iot_env) ---
# NOTE: The actual sensor library (board) requires Raspberry Pi hardware.
# We will use a try/except block to allow the script to run on your Windows laptop for testing.

try:
    # Attempt to import the hardware libraries (this will only succeed on the Raspberry Pi)
    import board
    import adafruit_bme680
    
    # Initialize the I2C communication interface (Standard way to talk to sensors)
    i2c = board.I2C() 
    # Create the BME680 sensor object
    bme680 = adafruit_bme680.Adafruit_BME680(i2c)
    
    # Set a name to show that the real hardware is being used
    SYSTEM_STATUS = "Running on Raspberry Pi"
    SIMULATION_MODE = False

# We now catch a broader range of exceptions, including the hardware-specific NotImplementedError,
# to force the script into simulation mode on Windows.
except (ImportError, NotImplementedError): 
    # This block executes if the script cannot find the 'board' library or is not on a Pi
    SYSTEM_STATUS = "Running in Windows Simulation Mode"
    SIMULATION_MODE = True

# --- MAIN READING LOOP ---
print("-" * 50)
print(f"Air Quality Reader Startup: {SYSTEM_STATUS}")
print("-" * 50)

# Set up a loop to run indefinitely (like a device that is always monitoring)
while True:
    
    # --- GET DATA (REAL OR SIMULATED) ---
    if SIMULATION_MODE:
        # If running on Windows, provide static/dummy data for testing the code logic
        temperature = 32.0 + (time.time() % 5) / 10  # Simulates small changes
        humidity = 55.0
        gas_resistance = 150000 
        pressure = 1013.25
        
    else:
        # If running on the Raspberry Pi, read the real sensor values
        temperature = bme680.temperature
        humidity = bme680.humidity
        pressure = bme680.pressure
        gas_resistance = bme680.gas

    # --- PROCESS AND DISPLAY DATA ---

    # 1. Temperature (Convert Celsius to Fahrenheit for easier reading)
    temp_f = (temperature * 9 / 5) + 32
    
    # 2. Gas Reading (The higher the resistance, the cleaner the air. Lower resistance means more VOCs)
    # We create a simple status message based on the raw gas reading
    if gas_resistance > 100000:
        gas_status = "Excellent"
    elif gas_resistance > 50000:
        gas_status = "Good"
    else:
        gas_status = "Moderate/Poor"

    # Print the results using f-strings (clean, organized output)
    print(f"[{time.strftime('%H:%M:%S')}]")
    print(f"  TEMP: {temp_f:.1f}°F (Humidity: {humidity:.1f}%)")
    print(f"  PRES: {pressure:.1f} hPa (Atmosphere)")
    print(f"  VOCs: {gas_status} (Resistance: {gas_resistance:.0f} ohms)")
    
    # --- CONTROL FLOW ---
    # The 'time.sleep()' function pauses the script for 5 seconds before the next loop
    time.sleep(5)