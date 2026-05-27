import asyncio
import sys

import websockets

from protocol.serialization import encode_message


async def main():
    payload = sys.stdin.buffer.read()

    message = {
        "type": "send",
        "station_id": b"test",
        "freq": 100,
        "payload": payload,
    }

    async with websockets.connect("ws://127.0.0.1:8765") as ws:
        await ws.send(encode_message(message))


asyncio.run(main())
