import tkinter as tk
from tkinter import scrolledtext
import threading
from scanner import scan_port, resolve_domain

def start_scan():
    target = entry_target.get()
    output.delete(1.0, tk.END)
    
    def run():
        ip = resolve_domain(target)
        if ip:
            output.insert(tk.END, f"[*] Scanning {target}...\n")
            ports = [21, 22, 23, 80, 443, 8080, 3306, 3389]
            for port in ports:
                try:
                    import socket
                    s = socket.socket()
                    s.settimeout(1)
                    s.connect((ip, port))
                    from services import SERVICES
                    service = SERVICES.get(port, "Unknown")
                    output.insert(tk.END, f"[+] Port {port} OPEN → {service}\n")
                    s.close()
                except:
                    output.insert(tk.END, f"[-] Port {port} CLOSED\n")
        else:
            output.insert(tk.END, "[-] Could not resolve target\n")
    
    threading.Thread(target=run).start()

# Window
window = tk.Tk()
window.title("Port Scanner")
window.geometry("600x400")
window.configure(bg="#1e1e1e")

# Title
title = tk.Label(window, text="Port Scanner", 
                 fg="#00ff00", bg="#1e1e1e", 
                 font=("Courier", 18, "bold"))
title.pack(pady=10)

# Input
frame = tk.Frame(window, bg="#1e1e1e")
frame.pack(pady=5)

tk.Label(frame, text="Target:", fg="white", 
         bg="#1e1e1e", font=("Courier", 12)).pack(side=tk.LEFT)

entry_target = tk.Entry(frame, width=30, 
                        font=("Courier", 12),
                        bg="#2d2d2d", fg="#00ff00",
                        insertbackground="white")
entry_target.pack(side=tk.LEFT, padx=5)

# Button
btn = tk.Button(window, text="SCAN", 
                command=start_scan,
                bg="#00ff00", fg="black",
                font=("Courier", 12, "bold"),
                padx=20)
btn.pack(pady=10)

# Output
output = scrolledtext.ScrolledText(window, 
                                    width=70, height=15,
                                    bg="#2d2d2d", fg="#00ff00",
                                    font=("Courier", 10))
output.pack(pady=10)

window.mainloop()
