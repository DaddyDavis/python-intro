import math

class RadioAntenna:
    """
    Blueprint for a VHF/UHF radio antenna object.
    Contains methods for calculating horizon distance based on height.
    """
    
    # The 'constructor' runs when you create a new object
    def __init__(self, name, height_feet):
        self.name = name
        self.height_feet = height_feet
        # The result will be stored here later
        self.horizon_distance_miles = 0.0

    # This is the METHOD (function) that belongs to the class
    def calculate_horizon(self):
        """Calculates line-of-sight distance using the 1.41 * sqrt(H) formula."""
        if self.height_feet <= 0:
            return 0.0
            
        # The core ham radio calculation
        self.horizon_distance_miles = 1.41 * math.sqrt(self.height_feet)
        return self.horizon_distance_miles
        
    # This method prints a formatted report
    def display_report(self):
        print("-" * 40)
        print(f"Antenna Model: {self.name}")
        print(f"Height Above Ground: {self.height_feet:.1f} feet")
        print(f"Max Horizon Distance: {self.horizon_distance_miles:.2f} miles")
        print("-" * 40)


# --- APPLICATION LOGIC (Creating the Objects) ---

print("--- AUSTIN'S OBJECT-ORIENTED RADIO LAB ---")

# 1. Create the Handheld OBJECT (Instance of the Class)
handheld_radio = RadioAntenna("Baofeng UV-26 (Handheld)", 10.0)

# 2. Create the Home Base OBJECT
home_base = RadioAntenna("Home Base (Tower)", 30.0)

# 3. Call the methods on the objects
handheld_radio.calculate_horizon()
home_base.calculate_horizon()

# 4. Display the results
handheld_radio.display_report()
home_base.display_report()


## 3. Run and Verify