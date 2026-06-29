import os
import requests

JSON_URL = "https://openai.com/chatgpt-connectors.json"
OUTPUT_FILE = "openai-ips.txt"

# Add standard web browser headers to bypass Cloudflare data center blocks
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

try:
    print(f"Fetching IP data from {JSON_URL}...")
    # Added headers and increased timeout parameter
    response = requests.get(JSON_URL, headers=HEADERS, timeout=20)
    
    # Debugging check: if Cloudflare blocks it, show the status code
    if response.status_code != 200:
        raise ValueError(f"Server returned status code {response.status_code}. Possible Cloudflare block.")
        
    data = response.json()
    
    prefixes = data.get("prefixes", [])
    ip_list = []
    for item in prefixes:
        ip = item.get("ip_prefix")
        if ip:
            ip_list.append(ip.strip())
            
    if not ip_list:
        raise ValueError("No IP prefixes found in the JSON file structure.")
        
    with open(OUTPUT_FILE, "w") as f:
        for ip in ip_list:
            f.write(f"{ip}\n")
            
    print(f"Successfully wrote {len(ip_list)} IPs to {OUTPUT_FILE}")

except Exception as e:
    print(f"Error processing EDL: {e}")
    exit(1)

