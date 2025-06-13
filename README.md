# port-scan
A practical Python project to learn network scanning using socket, regular expressions, and OSI Layer 2 concepts. Includes input validation, custom error handling, and uses tools like Wireshark to analyze packet behavior.

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
