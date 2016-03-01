import requests
import giphypop

g = giphypop.Giphy()

from scapy.all import *

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      if pkt[ARP].hwsrc == '00:00:00:00:00:00': # Kanye Button MAC
		kanye = g.screensaver('kanye west')
		url = 'https://maker.ifttt.com/trigger/button_pressed/with/key/[YOUR IFTTT KEY HERE]' + '?value1=' + kanye.media_url
		requests.post(url)
		print "KANYEBUTTON PRESSED"

print sniff(prn=arp_display, filter="arp", store=0)