from enum import IntEnum, auto


class Command(IntEnum):
    CREATE_STATION = 0
    EMIT = 1


class Event(IntEnum):
    SIGNAL = 0
    ERROR = 1
