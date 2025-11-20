def calculate_dipole(mhz):
    # Half-Wave Dipole (Total Length)
    # Formula: 468 / Freq (MHz)
    total_ft = 468 / mhz
    leg_ft = total_ft / 2
    leg_in = leg_ft * 12
    return total_ft, leg_in

def calculate_quarter_wave(mhz):
    # Quarter Wave Vertical (Car/HT Antenna)
    # Formula: 234 / Freq (MHz)
    length_ft = 234 / mhz
    length_in = length_ft * 12
    return length_ft, length_in

print("--- HAM RADIO CALCULATOR ---")
freq = float(input("Enter Frequency (MHz): "))

# Calculate
dipole_total, dipole_leg_in = calculate_dipole(freq)
vert_ft, vert_in = calculate_quarter_wave(freq)

print(f"\n--- RESULTS FOR {freq} MHz ---")
print(f"DIPOLE (Home Base):")
print(f"  Total Length: {dipole_total:.2f} ft")
print(f"  Each Leg:     {dipole_leg_in:.2f} inches")
print("")
print(f"QUARTER WAVE (Car/Mobile):")
print(f"  Vertical Element: {vert_in:.2f} inches")
print("-" * 30)