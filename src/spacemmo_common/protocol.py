"""
The SpaceFarer protocol is centered around JSON

Message destination
-------------------
    1 byte
    0x00 means direct
    else means relay (unsigned int)

Message destination name
------------------------
    only if destination != 0x00
    n-1 bytes (specified by destination)
    UTF-8 string data

Message length
--------------
    4 bytes
    unsigned little endian encoded int

Message data
------------
    n bytes (specified by message length)
    UTF-8 JSON data
"""


import json
from typing import Callable, Optional


def encode_message(message: dict, destination: Optional[str] = None):
    """
destination == None means direct message
"""
    result = b''

    if destination is None:
        result += b'\x00'
    else:
        dest_encoded = destination.encode('utf-8')
        result += (len(dest_encoded) + 1).to_bytes(1, 'little', signed=False)
        result += dest_encoded

    message_data = json.dumps(message).encode('utf-8')
    result += len(message_data).to_bytes(4, 'little', signed=False)
    result += message_data

    return result


def decode_message(read_function: Callable[[int], bytes]):
    destination_byte = read_function(1)
    if destination_byte == b'\x00':
        destination = None
    else:
        dest_length = int.from_bytes(destination_byte, 'little', signed=False) - 1
        destination = read_function(dest_length).decode('utf-8')

    message_length = int.from_bytes(read_function(4), 'little', signed=False)
    message = json.loads(read_function(message_length).decode('utf-8'))

    return destination, message


if __name__ == '__main__':
    message = encode_message({'label': 'value'})
    print(message)
    import io
    print(decode_message(io.BytesIO(message).read))
