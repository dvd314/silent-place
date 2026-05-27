import asyncio
import websockets

from protocol.serialization import decode_message


async def handler(ws):
    async for message in ws:
        data = decode_message(message)

        print(data)


async def main():
    async with websockets.serve(handler, "127.0.0.1", 8765):
        await asyncio.Future()


asyncio.run(main())
