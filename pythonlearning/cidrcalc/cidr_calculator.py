
import ipaddress
import csv

def cidr_calculator():
    """
    Calculates and displays network information for a given CIDR block.
    """
    try:
        cidr_input = input("Enter a CIDR block (e.g., 192.168.1.0/24): ")
        network = ipaddress.ip_network(cidr_input, strict=False)

        print(f"\nCIDR: {network.with_prefixlen}")
        print(f"Network Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Number of Hosts: {network.num_addresses - 2 if network.prefixlen < 31 else network.num_addresses}")
        print(f"Netmask: {network.netmask}")
        print(f"Hostmask: {network.hostmask}")
        print(f"Network part: {network.network_address}")
        print(f"Host part: {network.hostmask}")


        print("\nFirst 10 IP Addresses:")
        for i, ip in enumerate(network.hosts()):
            if i >= 10:
                break
            print(ip)

        generate_csv = input("\nDo you want to generate a CSV of all IP addresses in the network? (yes/no): ")
        if generate_csv.lower() == 'yes':
            generate_ip_csv(network)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def generate_ip_csv(network):
    """
    Generates a CSV file of all IP addresses in the network.
    """
    filename = f"{str(network.network_address).replace('.', '_')}_{network.prefixlen}_ips.csv"
    try:
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['IP Address'])
            for ip in network.hosts():
                csv_writer.writerow([str(ip)])
        print(f"\nSuccessfully generated {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    cidr_calculator()
