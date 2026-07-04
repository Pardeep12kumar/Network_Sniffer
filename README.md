# Network Packet Sniffer

## CodeAlpha Cyber Security Internship

A Python-Based Network Packet Sniffer developed using Scapy. this tool captures live network packets and displays useful information such as source IP, destination IP, protocol, ports, MAC addresses, packet length and maintains live protocol statistics.

---

## Features
1. Capture live network packets
2. Displays:
    - Timestamp
    - Source MAC Address
    - Destination MAC Address
    - Source IP Address
    - Destination IP Address
    - Protocol (TCP, UDP, ICMP, ARP)
    - Source Ports
    - Destination Ports
    - Packets Length
3. Live packet counters
4. Save packet information to:
    - CSV file
    - Text file 
5. Colored Terminal output using colorama

---
## Technologies Used
1. Python 3
2. Scapy
3. Colorama
4. Kali Linux

---
## Project Structure
Network_Sniffer/
|
|----packet_sniffer.py
|----logger.py
|----requirements.txt
|----packet.csv
|----packet.txt
|----README.md

---
## Create Virtual Enviroment 
'''bash
python3 -m venv venv
'''

## Activate Virtual Enviroment
'''bash
source venv/bin/activate
'''

## install Requirements
'''bash
pip install -y requirements.txt
'''
or install manually

'''bash
pip install scapy colorama
'''
---
##  Run The Project
'''bash
sudo python3 packet_sniffer.py
'''
Root privileges are required to captured network packets.

---

## Sample Output
'''
=======================
packet #15
=======================

Time            : 2026-07-05-   12:35:20
Source MAC      : 10:23:45:AA:11:22
Destination MAC : FF:FF:FF:FF:FF:FF
Source IP       : 192.168.1.5
Destination IP  : 8.8.8.8
Protocol        : UDP
Source port     : 54321
Destination port: 53
packet length   : 74 Bytes

====== LIVE STATISTICS ======
Total Packets   : 15
TCP Packets     : 9
UDP Packes      : 4
ICMP packets    : 1
ARP Packets     : 1
=========================
'''

---

## Clone the repository 
'''bash
https://github.com/pardeep24kumar/Network_Sniffer.git
cd Network_Sniffer

---

## Future improvement

1. GUI Interface 
2. Packet filtering 
3. Packet Search
4. save to PCAP file
5. Export to JSON
6. Traffic Graph


## Author 
Pardeep Kumar

