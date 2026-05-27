import asyncio
import sys

import websockets

from protocol.serialization import encode_packet
from protocol.packets import EmitPacket

async def main():
    payload = sys.stdin.buffer.read()

    message = EmitPacket(b'test', 10, 20, payload)

    async with websockets.connect("ws://127.0.0.1:8765") as ws:
        await ws.send(encode_packet(message))


asyncio.run(main())
