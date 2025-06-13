"""
This is a practical exercise that was heavily inspired from David Bombal https://www.youtube.com/watch?v=x4AE5yOF9pE&t=201s&ab_channel=DavidBombal.
Changes I made:
- Created exceptioins that notify user that the port number requirements (ascending order and port range).
- Changed port_range_pattern to .fullmatch to catch invalid input.
- Praticed writing basic code comments.
Goals of this project
- Understand Python as it pretains to networking.
- Understand input management using re.*
- Understand OSI Level 2 (Data Link) interactions within the OSI Model.
- Understand how socket.* methods and it's use in nmap.
- Use practical tools like 
	- Wireshark
		- Dropped SYN packets
		- 3 way handshakes
		- Filters to find sus packets on a network
	- Microsoft Command Prompt (ipconfig, ping)
	- Router managment
		- Manage router firewalls
		- Open ports
	- Firewalls (router, windows)
		- How packets are dropped by firewall.
	- Python TCP Listener.
		- ChatGPT created a TCP Listener to help with project. Opened port as listening to allow this application to scan port and for Wireshark to display scan.
"""

# Interface Berkeley sockets API
import socket
# Ensure input is correctly formatted.
import re

# IPv4 + port address validation
ip_address_pattern = re.compile("^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
# Setting the min and max ports.
port_min = 0
port_max = 65535

open_ports = []

while True:
	# Get the ip address from user, then breaking if we get a valid ip address.
	ip_address_entered = input("\nEnter IP address that you'd like to scan: ")
	if ip_address_pattern.search(ip_address_entered):
		print(f"{ip_address_entered} is a valid ip address.")
		break


while True:
	print("Enter range of ports you want to scan. Format: <int>-<int> (e.g. 20-40)")
	port_range = input("\nEnter port range: ")
	port_range_valid = port_range_pattern.fullmatch(port_range.replace(" ",""))
	if port_range_valid:
		port_min = int(port_range_valid.group(1))
		port_max = int(port_range_valid.group(2))

		if 0 <= port_min <= 65535 and 0 <= port_max <= 65535 and port_min <= port_max:
			# Valid, continue.
			break
		else:
			# Port numbers not 0-65535
			print("Port numbers must be 0 through 65535, and in ascending order. (not 500-10)")
	else:
		# Format is invalid.
		print("Invalid format. Please enter a port range like this 10-20.")

print(f"{port_min} - {port_max}")

for port in range(port_min, port_max + 1):
	try:
		# Create socket object

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.settimeout(0.5)
			s.connect((ip_address_entered, port))
			open_ports.append(port)
			# Assuming not errors packets flow as:
			# SYN -> SYN,ACK -> ACK

	except socket.timeout:
		print(f"Port {port} timed out.")
		# Connection to ip/port excedes s.settimeout() function.
		# (Host) SYN -> (Client) ---
	except ConnectionRefusedError:
		print(f"Port {port} is closed.")
		# - Not listening
		# - No service is running on that port
		# - Firewall not allowing connection
		# (Host) SYN-> (Client) RST, ACK
	except:
		pass
		# Catch all, accept error but do not crash.

#Finally report to the user the ports.
for port in open_ports:
	print(f"Port {port} is open on {ip_address_entered}.")