NetAgent

NetAgent is a lightweight, multi-protocol networking tool that provides simple TCP, UDP, HTTP, and WebSocket communication handling using Python's asyncio.

Features

Supports multiple communication protocols:

TCP Server

UDP Server

HTTP Server

WebSocket Server

Fully asynchronous with Python's asyncio

Lightweight and easy to deploy

Installation

Clone the repository:

git clone https://github.com/yourusername/NetAgent.git
cd NetAgent

Ensure you have Python 3.10+ installed.

Usage

Run the main script to start all servers:

python main.py

Ports & Protocols

TCP: Port 9001

UDP: Port 9002

HTTP: Port 8080

WebSocket: Port 9003

File Structure

NetAgent/
│── agents/
│   ├── tcp_agent.py
│   ├── udp_agent.py
│   ├── http_agent.py
│   ├── websocket_agent.py
│── main.py
│── README.md

Dependencies

This project uses asyncio and websockets. Install dependencies with:

pip install websockets

Contributing

Feel free to submit pull requests or open issues.


Author

zapper13 - https://github.com/zapper13

