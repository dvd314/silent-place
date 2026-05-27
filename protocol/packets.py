from dataclasses import dataclass


@dataclass(slots=True)
class EmitPacket:
    station_id: bytes
    freq: int
    strength: int
    payload: bytes

@dataclass(slots=True)
class SignalEvent:
    freq: int
    strength: int
    payload: bytes
