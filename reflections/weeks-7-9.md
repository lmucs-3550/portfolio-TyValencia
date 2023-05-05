---
description: Feb 20–Mar 17 (enjoy spring break!)
---

# Weeks 7-9

**2-21**

_Routing_

Packet:

* payload (the actual data)
* headers (metadata)
* destination address (must contain)
* implies that a host has one or more addresses

Router:

* an intermediate node that is usually connected to multiple neighbors
* way fewer links than full mesh
* more than a single link
* alternative paths

Forwarding packets: look in the forwarding table Things that could go wrong:

* network is partitioned
* router could fail/reboot
* implementation bug (misremembered number)
* packet drop
* link failure
* malicious actor (lying about number)

Bellman-Ford Algorithm - Distributed and asynchronous

Verifying routing state validity (diagram)

* dead ends and loops are obvious
* repeat for every destination



**2-23**

_IPs_

IP Addresses are heirarchical Networks that can be class A, B, or C based on how many devices connect

* class A supports 2^24 hosts and 2^7 networks
* class B supports 2^16 hosts and 2^14 networks
* class C supports 2^8 (254) hosts and 2^21 networks

IPv4 has 32 bits IPv6 gives us 128 bits Connects to whatever router is closest for the IP \~2,000 to 50,000 IP addresses at any given time at LMU

Mac address: 6 octets / 6 bytes (2^8 bits) 3C:5A:B4 - Google

* first three are based on who made them
* bits at the end are reserved for local network stuff
* 0: unicast, 1: multicast
* 0: globally unique, 1: locally administered

Address Resolution Protocol (ARP) How we discover other devices on our networks



**3-7**

_Sockets_

* OS abstraction for connections
* allow applications to operate on data streams (not packets)
* connect, listen, accept, send, receive

Open a source between source IP address: port and destination IP address: port

Sockets establish a connection (the basic abstraction)

* pipes data between two processes on different hosts
* data flows both ways
* communicate in bytes

Two types of sockets: server and client

* servers listen for clients to connect to them
* wait until a connection is attempted



**3-14**

_Congestion control_

* when queues get full

Packet loss becomes very noticeable very fast Need a discovery phase to find optimal paths

Possible approaches:

* send at will, lose excess
* reservations
* pricing/priorities
* dynamic adjustment (learn there is congestion)

Detect congestion when there is a loss or delay Do a combination of fast-multiplicative, slow-multiplicative, fast-additive, and slow-additive



**3-16**

_Congestion control cont._ How to have endhost adjust for congestion control?

Figure out optimal rate based on delay, not loss

TCP follows sawtooth behavior because of its AIMD protocol UDP does not recieve any acknowledgments and does not check congestion

* faster but less reliable
