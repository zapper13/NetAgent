import asyncio

class UDPHandler(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        """Called when the UDP socket is created"""
        self.transport = transport
        
    def datagram_received(self, data, addr):
        """Called when data is received"""
        print(f"[UDP] Received {data} from {addr}")

        response = b"Received: " + data
        self.transport.sendto(response, addr)