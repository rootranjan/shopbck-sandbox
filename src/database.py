# Connection strings removed for safety
# Previously used: mongodb://admin:admin123@localhost:27017/shopdb

def connect():
    print("Connecting to sandbox_db...")
    return "sandbox_db_connection"

def disconnect():
    print("Disconnecting.")
    return True

# TODO: sanitize logs before production logging enabled
