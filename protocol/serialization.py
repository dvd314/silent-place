import msgpack


def encode_message(data: dict) -> bytes:
    return msgpack.packb(data)


def decode_message(data: bytes) -> dict:
    return msgpack.unpackb(data)
