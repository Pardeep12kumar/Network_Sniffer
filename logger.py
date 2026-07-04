import csv
import os

OUTPUT_FOLDER = "output"

TEXT_FILE = os.path.join(OUTPUT_FOLDER, "packet.txt")
CSV_FILE = os.path.join(OUTPUT_FOLDER, "packet.csv")

def initialize_files():
    os.makedirs(OUTPUT_FOLDER, exist_ok = True)

    if not os.path.exists(TEXT_FILE):
         open(TEXT_FILE,"w" ).close()

    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w" , newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                
                "Time",
                "Source IP",
                "Destination IP",
                "Protocol",
            ])

def save_to_text(time, src, dst, protocol):
    with open(TEXT_FILE, "a", newline="")as file:
        file.write("=" * 60 + "\n")
        file.write(f"Time          :{time}\n")
        file.write(f"Source IP     :{src}\n")
        file.write(f"Destination IP: {dst}\n")
        file.write(f"Protocol      : {protocol}\n")
        

def save_to_csv(time, src, dst, protocol):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            
            time,
            src,
            dst,
            protocol
            
            
            
            ])