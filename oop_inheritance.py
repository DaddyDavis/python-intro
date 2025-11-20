import math

# --- 1. PARENT CLASS (The Blueprint) ---
class RadioAntenna:
    """The base class for any radio antenna, holding core data and methods."""
    
    # CONSTRUCTOR: Sets the name and height for ANY antenna
    def __init__(self, name, height_feet):
        self.name = name
        self.height_feet = height_feet
        self.horizon_distance_miles = 0.0

    # CORE METHOD: Calculates the distance (same for all antennas)
    def calculate_horizon(self):
        """Calculates line-of-sight distance using the 1.41 * sqrt(H) formula."""
        if self.height_feet <= 0:
            return 0.0
        self.horizon_distance_miles = 1.41 * math.sqrt(self.height_feet)
        return self.horizon_distance_miles
    
    def get_basic_report(self):
        return f"Antenna: {self.name} | Height: {self.height_feet:.1f} ft"


# --- 2. CHILD CLASS (Inherits from Parent) ---
class BaofengRadio(RadioAntenna):
    """
    A specialized class for your Baofeng HTs. 
    It inherits calculate_horizon() and get_basic_report() automatically.
    """
    def __init__(self, name, height_feet, model, power_watts):
        # Calls the PARENT class's constructor (RadioAntenna.__init__)
        super().__init__(name, height_feet) 
        self.model = model
        self.power_watts = power_watts
    
    # NEW METHOD: This is unique to the BaofengRadio class
    def display_full_specs(self):
        self.calculate_horizon() # Use the inherited method
        print("-" * 45)
        print(f"DEVICE: {self.name} ({self.model})")
        print(f"TX Power: {self.power_watts} Watts")
        print(f"Line of Sight: {self.horizon_distance_miles:.2f} miles")
        print("-" * 45)


# --- APPLICATION LOGIC (Creating the Specific Objects) ---

print("--- AUSTIN'S OOP INHERITANCE TEST ---")

# 1. Create a general object (uses only the PARENT class)
general_antenna = RadioAntenna("Simple Dipole", 45.0)
general_antenna.calculate_horizon()

# 2. Create a specialized object (uses the CHILD class, inheriting the math)
my_uv26 = BaofengRadio("My Baofeng HT", 6.5, "UV-26L", 5.0)

# --- DISPLAY RESULTS ---
print(f"\nParent Object Report: {general_antenna.get_basic_report()} | Horizon: {general_antenna.horizon_distance_miles:.2f} mi")

# Child object calls its own specialized report
my_uv26.display_full_specs()

## 3. Run and Verify