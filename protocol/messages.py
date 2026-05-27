from dataclasses import dataclass

@dataclass(slots=True)
class SendCommand:
    station_id: bytes
    freq: int
    payload: bytes
