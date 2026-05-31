import socket
import os
import csv
from datetime import datetime
SCAN_FILE = os.path.join(os .path.dirname(os.path.abspath(__file__)), "scans.txt")

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        results = sock.connect_ex((ip, port))
        sock.close()
        if results == 0:
             return True
        return False
    except Exception:

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except Exception:
        return "unknown"
    
def scan_host(ip):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 445, 3389]
    open_ports = []

    for port in common_ports:   
        if scan_port(ip, port):
            open_ports.append(port)

    hostname = get_hostname(ip)

    return {
        "ip": ip, 
        "hostname": hostname,
        "open_ports": open_ports
        "scan_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
def scan_network(base_ip, start, end):
    results = []

    for i in range(start, end + 1):
        ip = f"{base_ip}.{i}"
        print(f"Scanning {ip}...", end="\r")
        result = scan_host(ip)

        if result["open_ports"]:
            print(f"Open ports: {result['open_ports']}")
            results.append(result)  

    return results

def save_results(results):
    if not results:
        print("No results to save.")
        return
    
    with open(SCAN_FILE, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["IP", "Hostname", "Open Ports", "Scan Time"])
        for r in results:
            writer.writerow([
                r["ip"],
                r["hostname"],
                ", ".join(str(p) for p in r["open_ports"]),
                r["scan_time"]
            ])
    
    print(f"\nResults saved to:\n{SCAN_FILE}")

def main():
    print("\n--- Network Asset Scanner ---")
    base_ip = input("Enter network base IP (e.g. 192.168.1): ").strip()
    
    try:
        start = int(input("Start range (e.g. 1): ").strip())
        end = int(input("End range (e.g. 254): ").strip())
    except ValueError:
        print("Invalid range. Please enter numbers.")
        return
    
    results = scan_network(base_ip, start, end)
    
    if results:
        print(f"\n{len(results)} active hosts found.")
        save_results(results)
    else:
        print("\nNo active hosts found.")

if __name__ == "__main__":
    main()
