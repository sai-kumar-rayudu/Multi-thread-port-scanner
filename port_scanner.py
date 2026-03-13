#bin/python

import sys
from datetime import datetime
import socket
import threading
from queue import Queue


queue = Queue()
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
        print(f"Target or Port Error!: {port}")


def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()


if __name__ == "__main__":
    print("WELCOME TO PORT SCANNER")
    print("--" * 50)
    
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        target = input("Enter IP or Domain: ")
        print("Tip: You can specify target in the terminal")
        print("->python scanner.py IP or Domain")
        
    print("Scan initiated on:", datetime.now()) 
    print("--" * 50)
    print("Scanning...")
    
    for port in range(1, 1025):
        queue.put(port)
    
    #Using 100 threads
    for i in range(100):
        thread = threading.Thread(target=worker)
        thread.start()

    queue.join()

    print("\nScanning complete!")
    print("Open ports:", open_ports)
