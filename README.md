# py_port_scanner
Port scanners for detecting open ports on a network device

These scanners attempt to connect to hosts on the network through a selection of ports. If a successful connection is made, we know that the port is open.

## simple_scanner

The port range can be edited in `main.py` 

**1. Find the hosts on your network**
Run `arp -a` to find the hosts on your network.

The Address Resolution Protocol bridges the Data link (MAC and LLC - physical addressing) and Network (Path determination & IP - logical addressing) OSI layers.

**2. Install colorama**
If you want colours in your script add the colorama library.

**3. Run script**
Run script with ``python3 main.py``
