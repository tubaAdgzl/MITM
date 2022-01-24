import scapy.all as scapy
from scapy_http import http
import optparse

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i" ,"--interface" ,dest="user_iface" ,help="Enter interface ")

    input = parse_object.parse_args()[0]
    if not input.user_iface:
        print("Enter your interface!")

    return input

def packet_listener(user_iface):
    scapy.sniff(iface=user_iface,store=False,prn=analyze_packets)

def analyze_packets(packet):
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print(packet[scapy.Raw].load)

user_input = get_user_input()
user_interface = user_input.user_iface

try:
    packet_listener(user_interface)

except PermissionError:
    print("\nYou must be root!")
