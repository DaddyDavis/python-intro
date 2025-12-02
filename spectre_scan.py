import socket
import threading
from queue import Queue
from datetime import datetime

# --- CONFIGURATION (The "Control Panel") ---
target = "127.0.2.2"  # Scanning localhost (your Fedora VM) for now
# To scan your router later, you'd change this to "192.168.1.1" etc.

# We will scan ports 1 to 1024 (The "Well Known Ports")
# 22 = SSH, 80 = Web, 53 = DNS, etc.
queue = Queue()
open_ports = []

# --- THE "HACKER" AESTHETIC COLORS ---
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def port_scan(port):
    try:
        # Create a socket object (IPv4, TCP)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # Don't wait forever
        
        # Try to connect
        result = sock.connect_ex((target, port))
        
        if result == 0:
            return True
        sock.close()
    except:
        pass
    return False

# --- THE WORKER THREAD ---
def worker():
    while not queue.empty():
        port = queue.get()
        if port_scan(port):
            print(f"{GREEN}[+] Port {port} is OPEN{RESET}")
            open_ports.append(port)
        queue.task_done()

# --- MAIN EXECUTION ---
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Scan started at: {datetime.now()}")
print("-" * 50)

# 1. Fill the queue with jobs (Ports 1-1024)
for port in range(1, 1024):
    queue.put(port)

# 2. Create Threads (The "Army")
thread_list = []
for t in range(100): # Run 100 scans at once
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

# 3. Start the invasion
for thread in thread_list:
    thread.start()

# 4. Wait for everyone to finish
for thread in thread_list:
    thread.join()

print("-" * 50)
print(f"Scan Complete. Open Ports: {open_ports}")