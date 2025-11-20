import math

# --- 1. BASE CLASS ---
class RadioDevice:
    """The base class for any device. Defines the common command 'display_info'."""
    
    def __init__(self, name, height):
        self.name = name
        self.height = height
        
    # THE POLYMORPHIC METHOD: Generic information display
    def display_info(self):
        print(f"DEVICE: {self.name}")
        print(f"FUNCTION: General Radio Gear (Height: {self.height} ft)")


# --- 2. CHILD CLASS 1 (Amateur Radio) ---
class HamRadio(RadioDevice):
    """Specialized for amateur radio operators (like your Baofeng)."""
    
    def __init__(self, name, height, callsign):
        super().__init__(name, height)
        self.callsign = callsign

    # OVERRIDING THE PARENT'S METHOD
    # Same command name, different implementation
    def display_info(self):
        # Calculate Horizon here (Inherited logic)
        horizon = 1.41 * math.sqrt(self.height)
        print("-" * 35)
        print(f"[{self.callsign}]: {self.name} Status")
        print(f"TX Horizon: {horizon:.2f} miles")
        print(f"Type: VHF/UHF Handheld")


# --- 3. CHILD CLASS 2 (Networking/Server) ---
class WebServer(RadioDevice):
    """Specialized for network server (like your Flask app)."""
    
    def __init__(self, name, ip):
        super().__init__(name, 0) # Height is 0 for a server
        self.ip = ip

    # OVERRIDING THE PARENT'S METHOD
    # Same command name, different implementation
    def display_info(self):
        print("-" * 35)
        print(f"SERVER: {self.name} (Online)")
        print(f"IP: {self.ip}")
        print(f"Service: Flask Application")


# --- APPLICATION LOGIC (The Polymorphic Loop) ---
# Create a list of different objects
devices = [
    HamRadio("Baofeng UV-26L", 6.0, "W5DAV"), # Pretend callsign
    WebServer("Odin-Fedora-VM", "192.168.1.201"),
    RadioDevice("Unidentified Cable", 0.0) # Base device with simple info
]

print("--- RUNNING POLYMORPHIC DEVICE CHECK ---")

# We loop through all objects and run the SAME command: display_info()
# Each object automatically executes its OWN specialized version of the command.
for device in devices:
    device.display_info()

print("-" * 35)

## 3. Run and Verify