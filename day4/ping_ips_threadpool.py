import concurrent.futures
import re
import subprocess
import sys


def ping_ip(ip: str, count: int = 4) -> tuple[str, float]:
    """Ping an IP address `count` times and return (ip, success_percent)."""
    if sys.platform == "win32":
        cmd = ["ping", "-n", str(count), ip]
    else:
        cmd = ["ping", "-c", str(count), ip]

    result = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        errors="replace",
    )
    output = result.stdout + result.stderr

    # Parse packet loss percentage from output like "0.0% packet loss"
    match = re.search(r"(\d+(?:\.\d+)?)%\s+packet\s+loss", output, re.IGNORECASE)
    if match:
        loss_percent = float(match.group(1))
        success_percent = 100.0 - loss_percent
    else:
        # Could not parse output; assume total failure
        success_percent = 0.0

    print(f"IP = {ip}; success = {success_percent}")
    return ip, success_percent


def main():
    ips = [
        "8.8.8.8",          # Google DNS
        "8.8.4.4",          # Google DNS
        "1.1.1.1",          # Cloudflare DNS
        "1.0.0.1",          # Cloudflare DNS
        "9.9.9.9",          # Quad9 DNS
        "208.67.222.222",   # OpenDNS
        "208.67.220.220",   # OpenDNS
        "185.228.168.168",  # CleanBrowsing
        "185.228.169.169",  # CleanBrowsing
        "76.76.19.19",      # Control D
        "76.223.122.150",   # Control D
        "94.140.14.14",     # AdGuard DNS
        "94.140.15.15",     # AdGuard DNS
        "127.0.0.1",        # localhost
        "13.107.42.14",     # Microsoft
        "31.13.71.36",      # Facebook
        "157.240.11.35",    # Facebook
        "142.250.80.46",    # Google
        "142.250.185.78",   # Google
        "172.217.16.46",    # YouTube
        "151.101.1.140",    # Reddit
        "151.101.129.140",  # Reddit
        "104.244.42.193",   # X/Twitter
        "104.244.42.65",    # X/Twitter
        "140.82.121.4",     # GitHub
        "140.82.121.3",     # GitHub
        "52.94.236.248",    # Amazon
        "54.239.28.85",     # Amazon
        "13.225.63.117",    # Cloudfront
        "99.86.38.16",      # Cloudfront
    ]

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(ping_ip, ip) for ip in ips]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    for ip, success in results:
        print(f"{ip}: {success:.1f}% successful pings")


if __name__ == "__main__":
    main()
