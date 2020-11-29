# Tools for networking
Ping and Traceroute are two somewhat useful tools for looking at and learning about your network.

Ping sends a small packet to a host which may or may not choose to reply to it, and times how long the packet takes to get back. Lack of a reply doesn’t indicate a problem with the host or network.

Traceroute asks all routers along the path between you and the destination host if they'd like to respond to you, and times how long each of 3 requests take to get back to you. Some routers may not respond, but may still pass the traceroute packet along, and many hosts will not reply to the traceroute inquiry at all. Lack of a reply doesn't indicate a problem with the host or network.
