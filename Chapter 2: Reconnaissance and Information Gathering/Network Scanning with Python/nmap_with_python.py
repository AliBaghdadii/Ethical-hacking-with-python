import nmap

def nmap_scan(target, ports):
    nm = nmap.PortScanner()
    print(f"Scanning {target} for open TCP ports...")
    nm.scan(target, ports, arguments="-sV")

    for host in nm.all_hosts():
        print(f"Host: {host}")
        print(f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")

            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]["state"]
                service = nm[host][proto][port]["name"]
                version = nm[host][proto][port]["version"]
                print(f"Port {port}: {state} - {service} {version}")

# Example usage
target = "192.168.1.1"
ports = "21-25, 80, 443"
nmap_scan(target, ports)