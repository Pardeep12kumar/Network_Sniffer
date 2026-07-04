from packet_sniffer import start_sniffer

def main():


    while True:
        print("\n" + "=" * 60)
        print("     BASIC NETWORK SNIFFER")
        print("=" * 60)
        print("1. Capture All Packets")
        print("2. Capture TCP Packets")
        print("3. Capture UDP Packets")
        print("4. Capture ICMP Packets")
        print("5. Exit")
        
        choice = input("\n Enter the choice:    ")
        if choice == "1":
            start_sniffer()
            
        elif choice == "2":
            start_sniffer("tcp")

        elif choice == "3":
            start_sniffer("udp")

        elif choice == "4":
            start_sniffer("icmp")
        elif choice == "5":
            print("\nExiting ...    ")
            break
        
        else:
            print("Invalid Choice. Try Again")

if __name__ =='__main__':
    start_sniffer()