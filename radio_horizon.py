import math

print("--- AUSTIN'S VHF/UHF HORIZON CALCULATOR ---")
print("   Calculates Max Line-of-Sight Distance (in Miles)   ")
print("-" * 50)

# --- USER INPUT ---
try:
    height_feet_str = input("Enter Antenna Height (in feet): ")
    height_feet = float(height_feet_str)
    
except ValueError:
    print("\nError: Please enter a valid number for height.")
    exit()

# --- THE CALCULATION ---
# Formula: D (miles) = 1.41 * sqrt(H)
distance_miles = 1.41 * math.sqrt(height_feet)

# --- OUTPUT ---
print("-" * 50)
print(f"Antenna Height: {height_feet:.1f} feet")
print(f"Maximum Horizon Distance: {distance_miles:.2f} miles")

print("\n(Note: This is the distance from your antenna to the horizon.)")

## 3. Run and Verify

