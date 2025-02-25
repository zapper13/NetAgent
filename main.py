import sys
sys.path.append("agents")

import asyncio
import tcp_agent
import http_agent
import websocket_agent
from udp_agent import UDPHandler

async def main():
    loop = asyncio.get_running_loop()

    tcp_server = await asyncio.start_server(tcp_agent.handle_tcp_client, "0.0.0.0", 9001)
    print(f"[*] TCP Server listening on port 9001...")

    udp_transport, udp_protocol = await loop.create_datagram_endpoint(
        lambda: UDPHandler(),
        local_addr=("0.0.0.0", 9002)
    )
    print(f"[*] UDP Server listening on port 9002...")

    http_task = asyncio.create_task(http_agent.start_http_server(8080))
    print("[*] HTTP Server listening on port 8080...")

    ws_task = asyncio.create_task(websocket_agent.start_websocket_server(9003))
    
    async with tcp_server:
        await tcp_server.serve_forever()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("\n[*] Server shutting down.")
