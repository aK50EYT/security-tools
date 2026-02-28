import socket

# Dictionnaire des services
SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-ALT",
    3306: "MySQL",
    3389: "RDP",
    6379: "Redis",
    27017: "MongoDB"
}

def resolve_domain(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"[*] {target} resolved to {ip}")
        return ip
    except:
        print(f"[-] Could not resolve {target}")
        return None

def get_service(port):
    return SERVICES.get(port, "Unknown")

def scan_port(target, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        service = get_service(port)
        print(f"[+] Port {port} OPEN  →  {service}")
        s.close()
    except:
        print(f"[-] Port {port} CLOSED")

def scan_multiple_ports(target, ports):
    print(f"\n[*] Scanning {target}...\n")
    ip = resolve_domain(target)
    if ip:
        for port in ports:
            scan_port(ip, port)

target = input("Enter target IP or domain: ")
scan_multiple_ports(target, [21, 22, 23, 80, 443, 8080, 3306, 3389])
