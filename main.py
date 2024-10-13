import os
import platform
import time

# Determine the correct path to the hosts file based on OS
if platform.system() == "Windows":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
else:  # For macOS and Linux
    hosts_path = "/etc/hosts"

redirect = "127.0.0.1"


def block_websites(sites):
    with open(hosts_path, "r+") as file:
        content = file.read()
        for site in sites:
            if site not in content:
                file.write(f"{redirect} {site}\n")


def unblock_websites(sites):
    with open(hosts_path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(site in line for site in sites):
                file.write(line)
        file.truncate()


def main():
    with open("block_sites.txt", "r") as f:
        sites_to_block = [line.strip() for line in f.readlines()]

    # Block websites
    block_websites(sites_to_block)
    print("Websites blocked.")

    # try:
    #     while True:
    #         time.sleep(60)  # Check every minute
    # except KeyboardInterrupt:
    #     unblock_websites(sites_to_block)
    #     print("Websites unblocked.")


if __name__ == "__main__":
    main()
