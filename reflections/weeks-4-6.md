---
description: Jan 30–Feb 17
---

# Weeks 4-6

**1-31**

IPv6

* needs to be backward compatible in order to function
* protocol that keeps track of the state of the network in IP step



**2-2**

End hosts: Physical

* routers

Data link

* gets the data to the IP

IP

* stitching together different kinds of networks
* Gets the packets end to end with the best effort

Transport

* reliable delivery implemented at the transport or application layer

Sockets have allotted port numbers Once established between the web server and client, the client tells them their IP 65,000 possible port numbers

Router vs switch Router - implements IP, Ethernet, and physical layers Switch - implements ethernet at the local level (could have IP implemented) Old school switches could only be used at the local level

Layers with protocols 7. HTTP messages - both running code that implements the HTTP protocol 4. TCP bytestream - communicates to get all the info to put the packets back together 3. IP packets 2. Ethernet frames (packets at the ethernet level)

1. Physical

Between the ethernet and physical, OTN and optical protocols and be implemented OTN - both routers need to speak OTN Ethernet cannot coexist with OTN

USB3

* only 3m long Ethernet
* can be up to 100m
* connects you to a switch
* more reliable than wifi
* twisted-pair copper cable



**2-7**

Network communication:

1. Message response - specific to one address
2. Token - can be heard by everyone

_Partitioning:_ Space:

* frequency division multiplexing (FDM)
* electromagnetic waves are limited
* potentially wasteful due to dibs system

Time:

* time division multiplexing (TDM)
* turn taking
* slots
* random access

Carrier sense multiple access (CSMA/CD)

* listens first to see if any other hosts are communicating
* collision detection can occur with propagation delay

Ethernet addresses: list of hex digits 2 bits: flags 22 bits: company/manufacturer 24 bits: device-specific

Service types: Unicast - one recipient Anycast - send to any in a group Multicast - send to all in a group Broadcast - send to everyone



**2-14** Cyclic redundancy checks:

* single-bit errors
* double bit errors
* odd number of errors
* burst errors

checkSum - add up all the words that are transmitted and then transmit the result of that sum

Implementing reliability: Modern Ethernet implements switches to manage traffic

* no collisions
* similar protocol

802.11/wifi

* Standard, defines different physical layers that operate in various frequency bands and provide a range of different routes
