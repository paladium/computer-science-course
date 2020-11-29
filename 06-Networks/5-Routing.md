# IP Routing
As mentioned before, you can only send ethernet packets out of your ethernet interface, and ethernet packets stay on your local network.
You can put an IP (Network layer) packet inside of an ethernet (data layer) packet, but somebody's got to pass it along, and that somebody's a router.
Every IP number not on your local network will "belong" to your router in your ARP table.
If you want to talk to someone outside your local network, you'll send that ethernet packet to your router's ethernet address and trust that it will work afterwards. It's out of your hands now.

It knows which is a public and which is a private using mask, but there is a simple list to remember for private IP addresses:
1. 10.0.0.0 to 10.255.255.255
2. 172.16.0.0 to 172.31.255.255
3. 192.168.0.0 to 192.168.255.255

## Routers
Routers keep tables of networks, often many and often large.
Routers know: 1- Networks directly connected to them (sometimes one or two, sometimes a hundred or more), 2- Networks connected to their "friends and neighbors" and 3- The "default route" for everything else.

When your ethernet packet arrives at the router, it takes the Network packet (and all its contents), looks at the destination IP number, checks its tables, and sends a new ethernet (or other layer 2) packet (where the "sender" is now the router, not you) out the (hopefully) correct interface. That may go to the final host if it's on one of the routers directly connected networks, or to another router, which does the same process, until your packet gets to the router responsible for that local network, who then sends your packet to to the intended host. Whether your final destination host is in the next building or on the other side of the world, it works the same way.  
