A beginner-friendly Python project to explore network scanning using socket, regular expressions, and OSI Layer 2 concepts.
This tool includes input validation, exception handling, and integrates with Wireshark to help visualize network behavior.

**Inspiration**
This project was inspired by David Bombal's video.

**Changes & Improvements**
  - Added exception handling to alert users about invalid port ranges or descending order.
  - Used .fullmatch() for stricter regex input validation.
  - Added basic code comments for readability and learning.

**Goals of the Project**
  - Understand how Python applies to networking.
  - Practice managing input using re.*.
  - Explore OSI Layer 2 (Data Link Layer) behavior.
  - Learn how socket.* methods relate to tools like Nmap.
  - Use practical network analysis tools.

**Tools & Concepts Used**
  - Wireshark
  - Analyze SYN packets
  - Observe 3-way TCP handshakes
  - Filter suspicious packets
  - Command Line Tools
  - ipconfig, ping
  - Router Management
  - Open ports
  - Configure firewalls
  - Firewall Behavior
  - Understand how/why packets are dropped
  - Python TCP Listener
  - Created with ChatGPT to open ports and test scanner behavior via Wireshark
