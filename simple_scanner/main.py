"""Scan for open ports"""
import socket # python module for socket operations
from colorama import init, Fore # colors for our scan results

init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def find_open_ports(host, port):
    "detect whether host has any open ports"
    s = socket.socket() # new instance of socket
    try:
        s.connect((host,port))
        s.settimeout(0.2) # makes scanner faster but may be less accurate
    except:
        return False # port is closed
    else:
        return True # port is open
    
host = input("Enter the network host you want to scan:") # request user to input host
# print(host)
# print(type(host))
for port in range(1, 65535): # all ports
# for port in range(1,1023) # well-known ports
    if find_open_ports(host, port):
        print(f"{GREEN}[+] {host}:{port} is open {RESET}")
    else:
        print(f"{GRAY}[1] {host}:{port} is closed {RESET}", end="\r")
