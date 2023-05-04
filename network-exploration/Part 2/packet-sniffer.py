# Ty Valencia
# CMSI3550

from scapy.all import IP, TCP, wrpcap, sniff
from scapy.layers.http import HTTP
import sys
import os
import socket
import struct

def parsePCAP(pkts):
    for pkt in pkts:
        print("Source IP: " + pkt[IP].src)
        print("Destination IP: " + pkt[IP].dst)
        print("Source port: " + str(pkt[TCP].sport))
        print("Destinations port: " + str(pkt[TCP].dport))
        print("Packet Payload: " + str(pkt[TCP].payload))

def parsePCAP_mail(ip_address, pkts):
    mail_ports = [143, 25]
    mail_packets = [pkt for pkt in pkts if pkt[IP].src == ip_address and pkt[TCP].dport in mail_ports and len(pkt[TCP].payload) > 0]
    
    if mail_packets:
        filename = f"{ip_address}_mail_packets.pcap"
        wrpcap(filename, mail_packets)
        print(f"Saved {len(mail_packets)} mail packets from IP {ip_address} to file: {filename}")

def generate_files_for_ips(pkts):
    unique_src_ips = list(set([pkt[IP].src for pkt in pkts]))
    for ip in unique_src_ips:
        parsePCAP_mail(ip, pkts)

def parseReferer(pkts):
    referer_links = set()

    for pkt in pkts:
        if HTTP in pkt and 'Referer' in pkt[HTTP].fields:
            referer_links.add(pkt[HTTP].Referer)

    return referer_links


if __name__ == "__main__":
    pcap = sniff(count=100)  # Add this line to capture 100 packets, or adjust the count as needed
    parsePCAP(pcap)
    local_ip = get_local_ip()
    subnet_mask = "255.255.255.0" 
    print("\n")
    print("Scanning for other IPs in the local network:")
    findOtherIPs(local_ip, subnet_mask)
    print("\n")
    print("Generating mail packets files for unique IP addresses:")
    generate_files_for_ips(pcap)
    print("\n")
    print("Parsing Referer links from individual's packets:")
    referer_links = parseReferer(pcap)
    for link in referer_links:
        print(link)