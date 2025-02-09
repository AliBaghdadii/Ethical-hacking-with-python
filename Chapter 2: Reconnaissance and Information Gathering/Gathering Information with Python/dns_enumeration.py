import dns.resolver

def dns_enum(domain):
    record_types = ["A", "AAAA", "MX", "NS", "TXT"]
    
    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            print(f"{record_type} Records:")
            for rdata in answers:
                print(f" {rdata}")
        except dns.resolver.NoAnswer:
            print(f"No {record_type} record found")
        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain} does not exist")
        except Exception as e:
            print(f"Error: {e}")
        print()

dns_enum("example.com")