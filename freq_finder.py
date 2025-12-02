import webbrowser
import time

# --- CONFIGURATION ---
USER_ZIP = "39451"  # Leakesville, MS
USER_LAT = "31.1563"
USER_LON = "-88.5561"

# --- NATIONAL ACTIVE FREQUENCIES (Work Everywhere) ---
# Program these into your UV-26L immediately.
common_freqs = [
    {"name": "National 2m Call", "freq": "146.520", "mode": "FM", "desc": "Main Ham Calling Freq"},
    {"name": "National 70cm Call", "freq": "446.000", "mode": "FM", "desc": "UHF Ham Calling Freq"},
    {"name": "ISS Voice", "freq": "145.800", "mode": "FM", "desc": "Space Station Downlink"},
    {"name": "MURS Ch 1", "freq": "151.820", "mode": "FM", "desc": "License-Free VHF"},
    {"name": "GMRS/FRS 1", "freq": "462.5625", "mode": "FM", "desc": "Walkie Talkies / Hikers"},
    {"name": "Marine Ch 16", "freq": "156.800", "mode": "FM", "desc": "Boats/Coast Guard (Emergency)"},
    {"name": "Air Emergency", "freq": "121.500", "mode": "AM", "desc": "Civil Air Guard (Listen Only!)"},
    {"name": "NOAA Weather", "freq": "162.550", "mode": "FM", "desc": "WX Broadcast"},
]

def print_banner():
    print("="*60)
    print(f"📻 UV-26L FREQUENCY SEARCH TOOL | ZIP: {USER_ZIP}")
    print("="*60)

def show_common_list():
    print(f"\n[+] NATIONAL ACTIVE FREQUENCIES (Safe Bets):")
    print(f"{'NAME':<20} | {'FREQ (MHz)':<10} | {'MODE':<5} | {'DESCRIPTION'}")
    print("-" * 60)
    for f in common_freqs:
        print(f"{f['name']:<20} | {f['freq']:<10} | {f['mode']:<5} | {f['desc']}")
    print("-" * 60)
    print("💡 TIP: On your UV-26L, ensure 'AM' mode is on for 108-136 MHz.")

def open_local_databases():
    """
    Since RadioReference and RepeaterBook APIs are paid/restricted,
    we automate the browser to open the EXACT search pages for your area.
    """
    print(f"\n[+] LAUNCHING LOCAL SEARCH FOR ZIP {USER_ZIP}...")
    time.sleep(1)
    
    # 1. RadioReference (Greene County, MS Public Safety)
    # This is where you find Sheriff, Fire, and EMS frequencies.
    print(f"   -> Opening Greene County Public Safety database...")
    rr_url = "https://www.radioreference.com/db/browse/ctid/1411"
    webbrowser.open(rr_url)
    
    # 2. RepeaterBook (Local Ham Repeaters)
    # Searches for repeaters within 35 miles of Leakesville
    print(f"   -> Opening RepeaterBook (Proximity Search)...")
    rb_url = f"https://www.repeaterbook.com/repeaters/prox_result.php?city={USER_ZIP}&lat={USER_LAT}&long={USER_LON}&distance=35&band=144&freq=&call=&features=&status_id=%25&use=%25&order=distance_calc"
    webbrowser.open(rb_url)

    # 3. AirNav (Local Airports)
    # Finds nearby airports for Tower/Approach frequencies
    print(f"   -> Opening AirNav for local airports...")
    air_url = "https://www.airnav.com/airports/get?q=39451"
    webbrowser.open(air_url)

if __name__ == "__main__":
    print_banner()
    show_common_list()
    
    check = input("\nRun online local database search? (y/n): ")
    if check.lower() == 'y':
        open_local_databases()
        print("\n✅ Browser tabs opened. Look for 'Output Freq' and 'Tone'.")