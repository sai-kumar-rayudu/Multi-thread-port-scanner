import sys
from datetime import datetime
import socket


open_ports = []


def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)

        s.close()

    except:
        print("Target or Port Error!: Target should be IP or Domain.")


def scan(target):

    for port in range(1, 1024):
        scan_port(port)
            
    return
    

if __name__ == "__main__":
    print("WELCOME TO PORT SCANNER")
    print("- " * 50)
    
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        target = input("Enter IP or Domain: ")
        print("Tip: You can specify target in the terminal")
        print("->python scanner.py IP or Domain")
    print("Scan initiated on:", datetime.now()) 
    print("- " * 50)
    
    scan(target)
    
    print("Open ports are: ", open_ports)



