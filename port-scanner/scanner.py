import socket

def scan_port(target, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        print(f"[+] Port {port} OPEN")
        s.close()
    except:
        print(f"[-] Port {port} CLOSED")

def scan_multiple_ports(target, ports):
    print(f"\n[*] Scanning {target}...\n")
    for port in ports:
        scan_port(target, port)

target = input("Enter target IP: ")
scan_multiple_ports(target, [21, 22, 23, 80, 443, 8080])







