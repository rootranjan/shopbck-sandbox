# ⚠️ No CSRF protection
# TODO: Add HTML escaping to prevent injection

def validate(data):
    return all(data.values()) if isinstance(data, dict) else False

def debug_form(data):
    print("Form Data:", data)  # Dangerous in logs
