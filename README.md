Multi-Threaded Port Scanner
Overview

This project is a Python-based multi-threaded TCP port scanner that identifies open ports on a target system. The tool scans a range of ports concurrently using multiple threads, making the scanning process significantly faster than a traditional sequential port scanner.

The program attempts to establish a TCP connection with each port on the target host. If the connection is successful, the port is identified as open and displayed in the output.

This project demonstrates basic network reconnaissance techniques, socket programming, and concurrent execution using threading.

Features

Multi-threaded port scanning for faster execution

Scans ports 1–1024 (well-known ports)

Accepts target IP address or domain name

Supports command-line argument input

Displays open ports found during the scan

Uses a queue-based task system for efficient thread management

Prints scan start time and results

Technologies Used

Python

Socket Programming

Threading

Queue for task management

Command-line arguments (sys)

Date and time tracking (datetime)

How It Works

The user provides a target IP address or domain name.

Ports 1–1024 are added to a task queue.

100 worker threads are created.

Each thread retrieves a port from the queue and attempts to connect using a TCP socket.

If the connection succeeds, the port is marked as open.

After all ports are scanned, the program prints the list of open ports.

Usage

Run the scanner using a command-line argument:

python scanner.py <target_ip_or_domain>

Example:

python scanner.py scanme.nmap.org

Or run without arguments and enter the target when prompted:

python scanner.py
Example Output
WELCOME TO PORT SCANNER
--------------------------------------------------
Scan initiated on: 2026-03-13 12:15:21
Scanning...

Port 22 is OPEN
Port 80 is OPEN
Port 443 is OPEN

Scanning complete!
Open ports: [22, 80, 443]
Learning Objectives

This project helped practice:

Understanding how TCP connections work

Using Python sockets for network communication

Implementing multi-threading for concurrent tasks

Managing threads with queues

Basic network security reconnaissance techniques

Disclaimer

This tool is intended for educational purposes only. Only scan systems that you own or have permission to test.
