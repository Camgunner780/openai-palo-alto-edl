import os
import requests

JSON_URL = "https://openai.com"
# GitHub Pages can host directly from the main root directory
OUTPUT_FILE = "openai-ips.txt"

try:
    print(f"Fetching IP data from {JSON_URL}...")
    response = requests.get(JSON_URL, timeout=15)
    response.raise_for_status()
    data = response.json()
    
    prefixes = data.get("prefixes", [])
    ip_list = []
    for item in prefixes:
        ip = item.get("ip_prefix")
        if ip:
            ip_list.append(ip.strip())
            
    if not ip_list:
        raise ValueError("No IP prefixes found in the JSON file.")
        
    with open(OUTPUT_FILE, "w") as f:
        for ip in ip_list:
            f.write(f"{ip}\n")
            
    print(f"Successfully wrote {len(ip_list)} IPs to {OUTPUT_FILE}")

except Exception as e:
    print(f"Error processing EDL: {e}")
    exit(1)
