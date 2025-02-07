import requests
import socket

# If_Else Statements
port_open = False
port_filtered = False

if port_open:
    print("Port is open")
elif port_filtered:
    print("Port is filtered")
else:
    print("Port is closed")

# For Loops
open_ports = [22, 80, 443]  # Example list of open ports
for port in open_ports:
    print(f"Port {port} is open")

# While Loops
connected = False
attempts = 0

while not connected:
    print("Connecting...")
    attempts += 1

# Try/Except Blocks
target_url = "http://example.com"

try:
    response = requests.send_request(target_url)
except ConnectionError:
    print("Failed to connect to the target")
except TimeoutError:
    print("Request timed out")

# Functions
def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return True
        else:
            return False
    except:
        return False
    finally:
        sock.close()

# Using the function
if scan_port("192.168.1.1", 80):
    print("Port 80 is open")
else:
    print("Port 80 is closed")

# An example of using Requests library to perform a basic HTTP GET request
def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully connected to {url}")
        else:
            print(f"Failed to connect to {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Using the function
check_website("http://example.com")