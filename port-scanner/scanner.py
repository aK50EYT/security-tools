import socket
from services import SERVICES

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
