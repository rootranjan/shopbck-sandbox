# Legacy login logic (to be replaced by OAuth)
# WARNING: Do not use in production. No salt, no hashing.

def login(user, password):
    if user == "admin" and password == "admin123":
        return True  # 😱 Hardcoded credentials
    return False

# TODO: migrate to token-based login
