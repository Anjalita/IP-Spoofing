from scapy.all import *

# Create IP layer
ip = IP()
ip.src = "8.8.8.8"         # FAKE IP (Google)
ip.dst = "192.168.31.53"    # VICTIM IP (change to your target)

# Create ICMP layer (ping packet)
icmp = ICMP()

# Combine and send the packet
pkt = ip/icmp
send(pkt, count=4)



