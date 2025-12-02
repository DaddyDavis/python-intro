from flask import Flask, render_template_string
import socket
import threading
from queue import Queue

app = Flask(__name__)

# --- SCANNER ENGINE ---
def scan_target(target_ip):
    open_ports = []
    queue = Queue()
    
    # Scanning common ports (FTP, SSH, DNS, HTTP, RDP, etc.)
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3306, 3389, 8080]
    for p in common_ports:
        queue.put(p)

    def worker():
        while not queue.empty():
            port = queue.get()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            # connect_ex returns 0 if the connection is successful (Port Open)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "Unknown"
                open_ports.append((port, service))
            sock.close()
            queue.task_done()

    # Launch 20 Threads for speed
    for _ in range(20):
        t = threading.Thread(target=worker)
        t.start()
        
    queue.join()
    return sorted(open_ports)

# --- THE WEBSITE TEMPLATE (HTML + CSS) ---
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Spectre Command Center</title>
    <style>
        body { background-color: #0d1117; color: #00ff41; font-family: 'Courier New', monospace; padding: 20px; }
        h1 { border-bottom: 2px solid #00ff41; padding-bottom: 10px; }
        .card { background-color: #161b22; border: 1px solid #30363d; padding: 15px; margin-top: 20px; border-radius: 6px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { text-align: left; padding: 12px; border-bottom: 1px solid #30363d; }
        th { color: #ffffff; }
        .status-open { color: #00ff41; font-weight: bold; }
        .scan-btn { background-color: #238636; color: white; padding: 10px 20px; border: none; border-radius: 6px; cursor: pointer; font-size: 16px; text-decoration: none; display: inline-block; }
        .scan-btn:hover { background-color: #2ea043; }
    </style>
</head>
<body>
    <h1>Spectre Command Center</h1>
    <p>System: Fedora 43 Node | Operator: Austin</p>
    
    <div class="card">
        <h3>Target: Windows Host (10.0.2.2)</h3>
        <a href="/scan" class="scan-btn">INITIATE SCAN</a>
    </div>

    {% if ports is not none %}
    <div class="card">
        <h3>Scan Results</h3>
        <table>
            <tr>
                <th>Port</th>
                <th>Service</th>
                <th>Status</th>
            </tr>
            {% for port, service in ports %}
            <tr>
                <td>{{ port }}</td>
                <td>{{ service }}</td>
                <td class="status-open">OPEN</td>
            </tr>
            {% endfor %}
        </table>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def home():
    # Show the dashboard without results first
    return render_template_string(html_template, ports=None)

@app.route('/scan')
def do_scan():
    # Scan the Windows Gateway (10.0.2.2 is your Laptop's IP from inside the VM)
    results = scan_target("127.0.0.1")
    return render_template_string(html_template, ports=results)

if __name__ == '__main__':
    # Run on 0.0.0.0 so we can reach it from Windows
    app.run(host='0.0.0.0', port=5000)