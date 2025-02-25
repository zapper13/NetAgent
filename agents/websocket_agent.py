import asyncio
import websockets

async def handle_client(websocket): 
    print(f"[WebSocket] Connection from {websocket.remote_address}")

    try:
        async for message in websocket:
            print(f"[WebSocket] Received: {message}")
            await websocket.send(f"Echo: {message}")
    except websockets.exceptions.ConnectionClosed:
        print(f"[WebSocket] Client {websocket.remote_address} disconnected")

async def start_websocket_server(port=9003):
    """Starts the WebSocket server properly."""
    server = await websockets.serve(handle_client, "0.0.0.0", port)
    print(f"[*] WebSocket Server listening on port {port}...")
    await server.wait_closed()

