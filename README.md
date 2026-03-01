# Security Tools 🔒

A collection of offensive security tools for bug bounty and penetration testing.

## Tools

### Port Scanner
A Python-based port scanner with the following features:
- Scan multiple ports
- Domain name resolution
- Service detection (HTTP, SSH, FTP, MySQL...)
- Graphical User Interface (GUI)

## Usage

### CLI Mode
```bash
cd port-scanner
python scanner.py
```

### GUI Mode
```bash
cd port-scanner
python gui.py
```

## Screenshots

### GUI Interface
![Port Scanner GUI](screenshots/gui.png)

## Project Structure
```
security-tools/
    ├── port-scanner/
    │       ├── scanner.py    ← core scanning functions
    │       ├── services.py   ← ports and services dictionary
    │       └── gui.py        ← graphical interface
    └── README.md
```

## Author
- GitHub: aK50EYT-sec
- Email: anaskennouz7@gmail.com

## Legal Disclaimer
This tool is for educational purposes and authorized testing only.
Do not use against systems without explicit permission.
