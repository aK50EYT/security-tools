pythonimport socket

def scan_port(target, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        print(f"[+] Port {port} OPEN")
        s.close()
    except:
        print(f"[-] Port {port} CLOSED")

target = input("Enter target IP: ")
scan_port(target, 80)
