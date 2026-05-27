from dataclasses import dataclass


@dataclass(slots=True)
class Station:
    id: bytes

    x: int
    y: int

    vx: float
    vy: float

    last_update: float
