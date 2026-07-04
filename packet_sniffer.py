from scapy.all import sniff, IP, TCP, UDP, ICMP, Ether, ARP
from datetime import datetime
from logger import initialize_files, save_to_csv, save_to_text
from colorama import init, Fore, Style

init(autoreset=True)

# Packet Counters
packet_count = 0
tcp_count = 0
udp_count = 0
icmp_count = 0
arp_count = 0


def process_packet(packet):
    global packet_count, tcp_count, udp_count, icmp_count, arp_count

    # Count every packet
    packet_count += 1

    protocol = "Others"
    source_ip = "-"
    destination_ip = "-"
    source_port = "-"
    destination_port = "-"

    # MAC Addresses
    if packet.haslayer(Ether):
        source_mac = packet[Ether].src
        destination_mac = packet[Ether].dst
    else:
        source_mac = "-"
        destination_mac = "-"

    # IP Addresses
    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

    # Detect Protocol
    if packet.haslayer(TCP):
        protocol = "TCP"
        tcp_count += 1
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif packet.haslayer(UDP):
        protocol = "UDP"
        udp_count += 1
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif packet.haslayer(ICMP):
        protocol = "ICMP"
        icmp_count += 1

    elif packet.haslayer(ARP):
        protocol = "ARP"
        arp_count += 1

    packet_length = len(packet)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Live Statistics
    print(Fore.YELLOW + "\n========LIVE STATISTICS========")
    print(Fore.GREEN + f"Total Packets      :{packet_count}")
    print(Fore.BLUE +f"TCP Packets          :{tcp_count}")
    print(Fore.MAGENTA + f"UDP Packets      :{udp_count}")
    print(Fore.RED + f"ICMP Packets         :{icmp_count}")
    print(Fore.CYAN + f"ARP Packets         :{arp_count}")
    print(Fore.YELLOW + "================================\n")

    # Packet Details
    print(Fore.WHITE + "=" * 60)
    print(Fore.GREEN + f"Packet #{packet_count}")
    print(Fore.WHITE + "=" * 60)
    print(Fore.CYAN + f"Time             : {current_time}")
    print(Fore.YELLOW + f"Source MAC       : {source_mac}")
    print(Fore.YELLOW + f"Destination MAC  : {destination_mac}")
    print(Fore.YELLOW + f"Source IP        : {source_ip}")
    print(Fore.YELLOW + f"Destination IP   : {destination_ip}")
    print(Fore.MAGENTA + f"Protocol         : {protocol}")
    print(Fore.BLUE + f"Source Port      : {source_port}")
    print(Fore.BLUE + f"Destination Port : {destination_port}")
    print(Fore.WHITE + f"Packet Length    : {packet_length} Bytes")
    print(Fore.WHITE + "=" * 60)

    # Save Logs
    save_to_text(
        current_time,
        source_ip,
        destination_ip,
        protocol
    )

    save_to_csv(
        current_time,
        source_ip,
        destination_ip,
        protocol
    )


def start_sniffer():
    initialize_files()

    print(Fore.CYAN + "\nStarting Network Sniffer...")
    print(Fore.GREEN + "Press Ctrl + C to stop.\n")

    try:
        sniff(
            prn=process_packet,
            store=False
        )
    except KeyboardInterrupt:
        print("\nCapture Stopped.")

        print("\n========== FINAL STATISTICS ==========")
        print(f"Total Packets : {packet_count}")
        print(f"TCP Packets   : {tcp_count}")
        print(f"UDP Packets   : {udp_count}")
        print(f"ICMP Packets  : {icmp_count}")
        print(f"ARP Packets   : {arp_count}")
        print("======================================")


if __name__ == "__main__":
    start_sniffer()