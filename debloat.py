import subprocess
from ppadb.client import Client as AdbClient

# Connect to ADB
client = AdbClient(host="127.0.0.1", port=5037)
try:
    device = client.devices()[0]
    print(f"🚀 Connected to: {device.shell('getprop ro.product.model').strip()}")
except:
    print("❌ No phone found. Connect USB and enable Debugging.")
    exit()

# The "Hit List" - Add any package names here!
bloatware_list = [
    # CARRIER / SPYWARE
    "com.hth.airvoice_wireless",
    "com.hugoteam.airtalk_wireless",
    "com.airtalk.welcome",
    "android.autoinstalls.config.FOXXD.AS65U",
    "com.ddu.browser.oversea",
    "com.ddu.appstore",
    "com.ddu.android.weather",
    
    # UNISOC LOGGERS
    "com.sprd.logmanager",
    "com.sprd.linkturbo",
    "com.sprd.validationtools",
    "com.unisoc.silent.reboot",
    
    # THEMES
    "com.freeme.theme.oversea.elements",
    "com.freeme.theme.oversea.ziqiong",
    "com.freeme.theme.oversea.mountain",
    
    # HEAVY GOOGLE APPS
    "com.google.android.googlequicksearchbox", # Main Google App
    "com.google.android.gm",                   # Gmail
    "com.google.android.apps.maps",            # Maps
    "com.google.android.apps.photos",          # Photos
    "com.google.android.apps.wellbeing",       # Digital Wellbeing
    "com.google.android.apps.youtube.music",   # YouTube Music
    "com.google.android.videos"                # Google TV
]

print(f"💣 Prepared to nuke {len(bloatware_list)} apps...")

for app in bloatware_list:
    print(f"Targeting {app}...", end=" ")
    # Run the uninstall command
    # We use the '-k --user 0' flags to keep data but remove for current user
    result = device.shell(f"pm uninstall -k --user 0 {app}")
    
    if "Success" in result:
        print("✅ DELETED")
    else:
        print("⚠️ Not Found / Already Gone")

print("\n🎉 Debloat Complete! Rebooting phone now...")
device.shell("reboot")