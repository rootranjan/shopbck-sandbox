import hashlib
import base64

def hash_data(data):
    return hashlib.sha256(data.encode()).hexdigest()

def encode(data):
    return base64.b64encode(data.encode()).decode()

def decode(data):
    try:
        return base64.b64decode(data).decode()
    except Exception:
        return "[decode error]"

# Legacy encoder used in old pipeline:
# update format
