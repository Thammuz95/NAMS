from scapy.all import sniff


def packet_callback(packet):
    """
    Callback function for processing captured packets.

    Parameters:
    packet (scapy.packet): Packet object captured by scapy

    Returns:
    void: Processes and displays packet details
    """
    # Check if the packet has an IP layer
    if packet.haslayer("IP"):
        ip_src = packet["IP"].src  # Extract source IP address
        ip_dst = packet["IP"].dst  # Extract destination IP address
        print(f"Packet captured: {ip_src} -> {ip_dst}")  # Display packet details


def traffic_analysis():
    """
    Captures and analyzes network traffic.

    Parameters:
    None

    Returns:
    void: Captures and processes network packets
    """
    print("Starting traffic analysis...")
    sniff(prn=packet_callback, count=10)  # Capture 10 packets and process each using packet_callback
