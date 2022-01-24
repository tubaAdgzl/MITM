# MITM
# Man in the middle  tool

*Use man in the middle tool with packet listener.*

show this help message ->  ``` python3 mitm.py --help or python3 mitm.py -h ```

for packet lister -> ``` python3 packet_listener.py --help or python3 packet_lister.py -h ```

>  -h, --help            show this help message and exit
  -t TARGET_IP, --target=TARGET_IP
                        Enter target ip address
  -g GATEWAY_IP, --gateway=GATEWAY_IP
                        Enter gateway ip address
                       
> -h, --help            show this help message and exit
  -i USER_IFACE, --interface=USER_IFACE
                        Enter interface
                        
                        
## USE 
``` python3 mitm.py -t *target_ip* -g *gateway_ip* ``` 

``` python3 packet_listener.py *user_interface* ```


### Requirements
pyton 3.8

scapy 2.4.5
