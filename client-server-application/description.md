---
description: description.md
---

# catan-server.py

catan-server.py sets up a board for Catan and allows other players to connect to it using a TCP connection. It sets up the board by creating 19 hexagon tiles. It then gives each of these tiles a value from 2-12, based on two die rolls. Players can connect using localhost 50000, and the game can be set up with 2-4 players. Players are then assigned an order to associate tiles with themselves randomly based on their dice rolls. There are some other commands in place, such as moving pieces during their turn, that would be implemented in a full version.

Another application I would like to implement in the future would be generating random numbers each turn and distributing materials to players' inventories.

{% embed url="https://github.com/lmucs-3550/portfolio-TyValencia/blob/main/client-server-application/catan-server.py" %}

