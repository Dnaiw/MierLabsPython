import json


def serialize(data):
    return json.dumps(data).encode()

def deserialize(bytes):
    return json.loads(bytes.decode())