import subprocess
import time
import sys

# --- CONFIGURATION ---
# Subnet confirmed: 10.0.2.x (VirtualBox network)
network = "192.168.1." 
start_ip = 1
end_ip = 255 # Scanning IPs 1 through 19 for initial test

print("-" * 40)
print(f"SCANNING NETWORK: {network}x")
print("-" * 40)

# Start the timer
start_time = time.time()

# The Loop
for ip_number in range(start_ip, end_ip):
    address = network + str(ip_number)
    
    # The Command: ping -c 1 (count 1) -W 1 (wait 1 sec)
    # We use subprocess to run the ping command
    res = subprocess.call(['ping', '-c', '1', '-W', '1', address], 
                          stdout=subprocess.DEVNULL, 
                          stderr=subprocess.DEVNULL)
    
    # Check the return code. 0 means SUCCESS (Host is ONLINE)
    if res == 0:
        print(f"[+] HOST ONLINE: {address}")
    # else:
    #    sys.stdout.write(".") # Optional dot to show progress
    #    sys.stdout.flush()

# End stats
duration = time.time() - start_time
print("-" * 40)
print(f"Scan Complete in {duration:.2f} seconds")