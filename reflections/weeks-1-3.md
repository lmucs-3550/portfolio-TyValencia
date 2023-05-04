---
description: Jan 9–27
---

# Weeks 1-3

Topics learned: 

**1-12/1-17**
Network: Any group of devices connected by a link
Protocols: structured communication
Internet: A group of networks
- transfers data between end hosts
- path must have no breaks 
- must follow protocols
- competition between ISPs
- Asynchronous
- IPv6 accomodates more IPs than IPv4


Layers of the internet: (top-down perspective)
L7: Application 
- Skype, Zoom, etc.
- can send app-specific protocols

L4: Transport 
- reliable delivery, requests data to resend
- can send TCP/UDP
- data transformed into packets through ports 
- time and reliablility is important

L3: Network 
- routing, how to get the path

L2: Link 
- getting data from one to the next
- ethernet, 802.11

L1: Physical
- optical, copper, radio


End hosts and switches are connected by links 
- bluetooth, cables, internet


**1-19**
Packet delay: 
Metadata needs to know:
- which protocol to use
- time-to-live
- IP
- destination address
- size

Bandwith: 
- width of a wire
- how many bits can be sent per unit of time

Propagation delay: 
- length of the link and the physics of the material
- how long it takes for bits to go from one side to the other

Bandwidth delay product = B x Pd

Switches only have network and IP layers


**1-24**
Routers:

Control plane
- computing tables with a routing algorithm
- only activates per network event

Data plane 
- local operation
- activates every time a packet arrives
- forwards packets to its forwarding table


**1-26**
Packet switching: sharing resources between packets
- don't need a dedicated channel
- dynamic bandwidth 
- packet loss

Circuit switching:
- more predictability and security than packet switching

The internet uses packet switching and is tolerant to packet loss
IPv4 -> IPv6 took a decade to implement

Packet delay: transmission delay + propagation delay + queueing delay

Local delivery: link specific (ethernet network)
Global delivery: Goes between ISPs in different regions to talk to other local spaces
