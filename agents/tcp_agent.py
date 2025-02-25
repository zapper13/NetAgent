import asyncio

async def handle_tcp_client(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"[TCP] Connection from {addr}")

    writer.write(b"Welcome to TCP\n")
    await writer.drain()

    while True:
        try:
            data = await reader.read(1024)
            if not data:
                break

            command = data.decode().strip()
            print(f"[TCP] Received from {addr}: {command}")

            response = f"TCP Echo: {command}".encode()
            writer.write(response + b"\n")
            await writer.drain()
        except:
            break

    print(f"[-] TCP Client {addr} disconnected")
    writer.close()
    await writer.wait_closed()
