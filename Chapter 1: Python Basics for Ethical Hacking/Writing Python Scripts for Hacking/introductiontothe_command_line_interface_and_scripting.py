import argparse
import socket

# Here's an example of a Python script that uses command-line arguments:

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def main():
    parser = argparse.ArgumentParser(description="Simple port scanner")
    parser.add_argument("target_ip", help="Target IP address to scan")
    parser.add_argument("-p", "--ports", type=int, nargs=2, default=[1, 1024]
                        , help="Port range to scan (default: 1-1024)")
    args = parser.parse_args()

    target_ip = args.target
    start_port, end_port = args.ports

    print(f"Scanning {target_ip} for open ports...")
    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            print(f"Port {port} is open")

if __name__ == "__main__":
    main()

# To run this script from the command line:
# python port_scanner.py 192.168.1.1 -p 1 100