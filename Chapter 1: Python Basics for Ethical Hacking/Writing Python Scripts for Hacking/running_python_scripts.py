import socket

# 1. Create a file named port_scanner.py with the following content:
def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

target_ip = "192.168.1.1"
for port in range(1, 1025):
    if scan_port(target_ip, port):
        print(f"Port {port} is open")

# 2. Open a terminal or command prompt
# 3. Navigate to the directory where you saved port_scanner.py
# 4. Run the script using the Python interpreter:
#    python port_scanner.py