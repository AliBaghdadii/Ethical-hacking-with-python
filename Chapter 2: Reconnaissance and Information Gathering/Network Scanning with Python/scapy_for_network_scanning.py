from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP

def tcp_syn_scan(target, ports):
    print(f"Scanning {target} for open TCP ports...")
    for port in ports:
        src_port = RandShort()
        resp = sr1(IP(dst=target)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
        if resp is None:
            print(f"Port {port} is filtered.")
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12: # SYN-ACK
                sr(IP(dst=target)/TCP(sport=src_port, dport=port, flags="R"), timeout=1, verbose=0)
                print(f"Port {port} is open.")
            elif resp.getlayer(TCP).flags == 0x14: # RST-ACK
                print(f"Port {port} is closed.")
        elif resp.haslayer(ICMP):
            if int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                print(f"Port {port} is filtered.")

# Example usage
target = "192.168.1.1"
ports = [21, 22, 23, 443, 3389]
tcp_syn_scan(target, ports)