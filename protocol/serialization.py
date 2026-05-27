import msgpack

from protocol.types import Command, Event
from protocol.packets import (
    EmitPacket,
    SignalEvent,
)


def encode_packet(packet) -> bytes:
    match packet:
        case EmitPacket():
            raw = [
                Command.EMIT,
                packet.station_id,
                packet.freq,
                packet.strength,
                packet.payload,
            ]

        case SignalEvent():
            raw = [
                Event.SIGNAL,
                packet.freq,
                packet.strength,
                packet.payload,
            ]

        case _:
            raise ValueError(f"cannot encode packet: {type(packet)}")

    return msgpack.packb(raw)


def decode_packet(raw: bytes):
    packet = msgpack.unpackb(raw)

    packet_type = packet[0]

    match packet_type:
        case Command.EMIT:
            return EmitPacket(
                station_id=packet[1],
                freq=packet[2],
                strength=packet[3],
                payload=packet[4],
            )

        case Event.SIGNAL:
            return SignalEvent(
                freq=packet[1],
                strength=packet[2],
                payload=packet[3],
            )

        case _:
            raise ValueError(f"unknown packet type: {packet_type}")
